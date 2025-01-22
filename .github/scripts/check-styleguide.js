const core = require('@actions/core');
const fs = require('fs');
const rules = require('./styleguide-rules.json');
const filePath = process.argv[2];

if (!filePath) {
    console.error('No file path provided.');
    process.exit(1);
}

if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
}

const content = fs.readFileSync(filePath, 'utf-8');

// Helper function to remove code blocks, inline code, and links
// while keeping track of the positions where we should skip style checking.
const getSanitizedRanges = (content) => {
    const ranges = [];

    // Match code blocks (```code```)
    const codeBlockMatches = [...content.matchAll(/```[\s\S]*?```/g)];
    codeBlockMatches.forEach((match) => {
        ranges.push([match.index, match.index + match[0].length]);
    });

    // Match inline code (`code`)
    const inlineCodeMatches = [...content.matchAll(/`[^`]*`/g)];
    inlineCodeMatches.forEach((match) => {
        ranges.push([match.index, match.index + match[0].length]);
    });

    // Match links [text](url)
    const linkMatches = [...content.matchAll(/\[([^\]]+?)\]\(.*?\)/g)];
    linkMatches.forEach((match) => {
        // Only sanitize the part that matches the URL, keeping the text for checking
        ranges.push([match.index + match[0].indexOf(']') + 1, match.index + match[0].length]);
    });

    // Match <a href="url">
    const anchorHrefMatches = [...content.matchAll(/<a\s+[^>]*href="([^"]*)"[^>]*>/gi)];
    anchorHrefMatches.forEach((match) => {
        const hrefStart = match.index + match[0].indexOf('href="') + 6;
        const hrefEnd = hrefStart + match[1].length;
        ranges.push([hrefStart, hrefEnd]);
    });

    return ranges;
};

// Check if a given index falls within a sanitized range
const isInSanitizedRange = (index, ranges) => {
    return ranges.some(([start, end]) => index >= start && index < end);
};

const escapePhrase = (string) => {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // Escape special characters
};

// Check for style violations, but skip sanitized content
const checkStyle = (content, ranges) => {
    const results = new Set();

    for (const [phrase, { replace, caseSensitive, note }] of Object.entries(rules)) {
        const regexFlags = caseSensitive ? 'g' : 'gi';
        const escapedPhrase = escapePhrase(phrase);

        const regex = new RegExp(`\\b${escapedPhrase}\\b`, regexFlags);

        let match;
        while ((match = regex.exec(content)) !== null) {
            const matchIndex = match.index;

            // Skip over sanitized sections
            if (isInSanitizedRange(matchIndex, ranges)) {
                continue;
            }

            const lineNumber = content.substring(0, match.index).split('\n').length;
            const columnNumber = match.index - content.lastIndexOf('\n', match.index);
            const suggestion = `Replace with "${Array.isArray(replace) ? replace.join(' or ') : replace}"`;
            const issue = `${filePath}:${lineNumber}:${columnNumber}:❌ **Found "${phrase}"**<br><br>${note}<br>💡 **Suggestion** - ${suggestion}.<br><br><blockquote>✍ Check the [Education Styleguide](https://www.notion.so/vtexhandbook/E-D-Style-Guide-80cf41f627574419bde54e64aa04d1df) for more information.</blockquote>`;

            // Add issue to the Set
            results.add(issue);
        }
    }

    return Array.from(results); // Convert Set back to array
};

// Get sanitized ranges to ignore during style checking
const sanitizedRanges = getSanitizedRanges(content);

// Check style in the original content, skipping sanitized ranges
const issues = checkStyle(content, sanitizedRanges);

if (issues.length > 0) {
    const formattedIssues = issues.join('\n');
    console.log(formattedIssues);
    core.setOutput('style-issues', formattedIssues);
    core.setFailed('Style issues detected.'); 
    process.exit(1); // Indicate that issues were found
} else {
    console.log('No style issues found.');
    process.exit(0); // Indicate success
}
