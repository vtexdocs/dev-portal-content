import fetch from "node-fetch";
import fs from "fs";
import core from "@actions/core";

const filePath = process.argv[2];

if (!filePath) {
  console.error("No file path provided.");
  process.exit(1);
}

if (!fs.existsSync(filePath)) {
  console.error(`File not found: ${filePath}`);
  process.exit(1);
}

const content = fs.readFileSync(filePath, "utf-8");

// Extract links from Markdown and HTML content
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

// Check if a link is broken (404 or other errors)
async function checkLink(url) {
  try {
    const response = await fetch(url);
    return { isValid: response.ok, statusCode: response.status }; 
  } catch (error) {
    console.error(`Error checking link ${url}: ${error.message}`);
    return false;
  }
}

// Main function to check links in a file
async function checkLinksInFile(content) {
  const links = extractLinks(content);
  const issues = [];

  for (const link of links) {
    const { isValid, statusCode } = await checkLink(link.url);
    if (!isValid) {
      // Format the issue message with line and column numbers
      const issue = `${filePath}:${link.lineNumber}:${link.columnNumber}:🚨 **Found a broken link in a ${link.type} (Error ${statusCode}):**<br> ${link.url}<br><br><blockquote>👉 Please review this link before merging your Pull Request.</blockquote>`;
      issues.push(issue);
    }
  }

  return issues;
}

(async () => {
    try {
      const issues = await checkLinksInFile(content);
      
      if (issues.length > 0) {
        console.log(`Broken links found in ${filePath}:`);
        const formattedIssues = issues.join("\n");
        core.setOutput('link-issues', formattedIssues);
        console.log(formattedIssues);
        process.exit(0);
      } else {
        console.log(`No broken links in ${filePath}`);
        process.exit(0); // Indicate success
      }
    } catch (error) {
      console.error(`An error occurred: ${error.message}`);
      process.exit(1); // Indicate failure due to error
    }
  })();