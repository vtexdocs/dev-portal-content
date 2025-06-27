---
title:"CSS Analysis"
---

To enforce proper containment and prevent global style leakage, the Analyzer supports CSS analysis. As shown in [step 1](#instructions) of the previous section, when calling `analyzeFiles()`, you can specify CSS analysis options:

```typescript
await analyzer.analyzeFiles({
  filePattern: 'your-module/**/*.{js,ts,jsx,tsx,css,less,scss}',
  cssOptions: {
    allowedNamespaces: ['extension-'], // Array of allowed CSS namespace prefixes
    transformNonCompliant: true, // Whether to automatically fix non-compliant CSS
    defaultNamespace: 'extension-', // Default namespace to add to selectors
    verbose: true, // Output details and write transformed files to disk
    overwriteTransformed: true, // Whether to overwrite existing transformed files
  }
});
```

### CSS Rules and enforcement

The Analyzer checks for the following types of CSS violations:

- **Global Selectors:** Restricts usage of global selectors like `*`, body, html, `:root` which could affect the entire page.
- **CSS Containment:** Prevents CSS from breaking out of its intended containment and affecting other parts of the page.
- **Namespace requirements:** Ensures all selectors are properly namespaced (example: `.extension-myClass` instead of `myClass`) to avoid collisions.
- **Restricted properties and values:** Blocs usage of CSS properties and values that could comprise the sandbox integrity.
- **Automatic transformation:** When `transformNonCompliant` is enabled, the Analyzer attempts to fix CSS issues by:
  - Adding the default namespace to class and ID selectors.
  - Namespacing [Keyframes](https://github.com/Keyframes) animations.
  - Replacing global element selectors with namespaced container classes.
  - Adding containment properties to ensure styles don’t leak.
- **Transformed files:** When both `transformNonCompliant` and `verbose` are true, the Analyzer writes transformed CSS to files with `.transformed.css` extension, which can be used in your build process or debugging. Example:
  - Original: `styles.css`
  - Transformed: `styles.transformed.css`

### Error handling

If violations are detected and `transformNonCompliant` is set to false, the Analyzer logs errors with detailed information. When `transformNonCompliant` is true, violations are fixed automatically and logged as warnings.

The analysis output includes:
- Total number of files analyzed.
- List of violations by file, if any.
- List of warnings by file, if any.
- Paths to transformed CSS files, when applicable.

### Best practices

- **Early detection:** Run CSS analysis during the pre-build stage to catch issues as early as possible.
- **Namespace everything:** Use your extension’s namespace prefix for all CSS selectors to avoid conflicts.
- **Avoid global selectors:** Don’t use universal `*` or document-level selectors like `html`, `body`, or `:root`.
- **Enable transformation:** Set `transformNonCompliant: true` in development to fix non-compliant styles.
- **Review transformed CSS:** Check the `.transformed.css` files to understand what was modified during the analysis.
