import fetch from "node-fetch";
import fs from "fs";
import path from "node:path";

const filePath = process.argv[2];
const issuesFile = process.env.LINK_ISSUES_FILE || "link_issues.txt";

if (!filePath) {
  console.error("No file path provided.");
  process.exit(1);
}

if (!fs.existsSync(filePath)) {
  console.error(`File not found: ${filePath}`);
  process.exit(1);
}

const content = fs.readFileSync(filePath, "utf-8");

const displayPath =
  path.relative(process.cwd(), path.resolve(filePath)).split(path.sep).join("/") ||
  filePath;

// Extract links from Markdown and HTML content
const extractLinks = (content) => {
  const linkRegex = /\[([^\]]+)\]\((https?:\/\/[^\)]+)\)/g; // Markdown links
  const anchorRegex = /<a[^>]+href=["'](https?:\/\/[^"']+)["'][^>]*>/g; // HTML anchor tags
  const markdownImageRegex = /!\[([^\]]*)\]\((https?:\/\/[^\)]+)\)/g; // Markdown images
  const imgTagRegex = /<img[^>]+src=["'](https?:\/\/[^"']+)["'][^>]*>/g; // HTML img tags

  const links = [];
  let match;

  // Helper function to calculate line and column number
  function getLineAndColumn(content, position) {
    const lines = content.slice(0, position).split("\n");
    const lineNumber = lines.length;
    const columnNumber = lines[lines.length - 1].length + 1;
    return { lineNumber, columnNumber };
  }

  // Find Markdown images first
  while ((match = markdownImageRegex.exec(content)) !== null) {
    const { lineNumber, columnNumber } = getLineAndColumn(content, match.index);
    links.push({
      type: "Markdown Image",
      url: match[2], // Use match[2] for the URL
      alt: match[1], // Use match[1] for the alt text
      lineNumber,
      columnNumber,
    });
  }

  // Then find Markdown links (ignoring already matched image URLs)
  while ((match = linkRegex.exec(content)) !== null) {
    const { lineNumber, columnNumber } = getLineAndColumn(content, match.index);
    // Ensure this URL is not already captured as an image
    if (!links.some(link => link.url === match[2] && link.type === "Markdown Image" && lineNumber === link.lineNumber)) {
      links.push({
        type: "Markdown Link",
        url: match[2],
        text: match[1],
        lineNumber,
        columnNumber,
      });
    }
  }

  // Find HTML anchor links
  while ((match = anchorRegex.exec(content)) !== null) {
    const { lineNumber, columnNumber } = getLineAndColumn(content, match.index);
    links.push({
      type: "HTML Anchor",
      url: match[1],
      text: "",
      lineNumber,
      columnNumber,
    });
  }

  // Find HTML img src
  while ((match = imgTagRegex.exec(content)) !== null) {
    const { lineNumber, columnNumber } = getLineAndColumn(content, match.index);
    links.push({
      type: "HTML Image",
      url: match[1],
      alt: "",
      lineNumber,
      columnNumber,
    });
  }

  return links;
};

const BROWSER_UA =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36";

async function fetchWithTimeout(url, options = {}, timeoutMs = 8000) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      redirect: "follow",
      headers: {
        "User-Agent": BROWSER_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        ...options.headers,
      },
      signal: controller.signal,
      ...options,
    });

    return response;
  } finally {
    clearTimeout(id);
  }
}

// Check if a link is broken (404 or other errors)
// states: "valid" | "invalid" | "unknown"
async function checkLink(url) {
  try {
    let response = await fetchWithTimeout(url, { method: "HEAD" });

    if (!response.ok && [405, 501].includes(response.status)) {
      response = await fetchWithTimeout(url, { method: "GET" });
    }

    const status = response.status;

    // likely auth / rate limit
    const ambiguous = [401, 403, 429];
    if (ambiguous.includes(status) || status >= 500) {
      return { state: "unknown", statusCode: status };
    }

    if (response.ok) {
      return { state: "valid", statusCode: status };
    }

    // e.g. 404, 410, 500, etc.
    return { state: "invalid", statusCode: status };
  } catch (error) {
    console.error(`Error checking link ${url}: ${error.message}`);

    return { state: "unknown", statusCode: null, error };
  }
}

// Main function to check links in a file
async function checkLinksInFile(content) {
  const links = extractLinks(content);
  const issues = [];

  for (const link of links) {
    const { state, statusCode } = await checkLink(link.url);
    if (state === "invalid") {
      const issue = `${displayPath}:${link.lineNumber}:${link.columnNumber}:🚨 **Found a broken link in a ${link.type} (Error ${statusCode}):**<br> ${link.url}<br><br><blockquote>👉 Please review this link before merging your Pull Request.</blockquote>`;
      issues.push(issue);
    } else if (state === "unknown") {
      console.error(`Could not reliably check link: ${link.url}`);
    }
  }

  return issues;
}

(async () => {
  try {
    const issues = await checkLinksInFile(content);

    if (issues.length > 0) {
      console.error(`Broken links found in ${displayPath}:`);
      const block = issues.join("\n") + "\n";
      fs.appendFileSync(issuesFile, block, "utf-8");
      process.exit(0);
    } else {
      console.error(`No broken links in ${displayPath}`);
      process.exit(0);
    }
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
    process.exit(1);
  }
})();
