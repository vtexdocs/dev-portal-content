---
title: "Implementing FastStore Analyzer"
---

In this guide, you will learn how to securely implement [Extension points](LINK) in [FastStore modules](LINK) by using FastStore Analyzer.

The FastStore Analyzer is a static analysis tool that helps maintain code quality and security in FastStore projects. By integrating it into your development workflow with customizable CLI hooks, it scans your codebase to identify issues before they affect your build.

Follow the steps below to implement FastStore Analyzer in your store.

## Before you begin

<Steps>

### Install the FastStore Platform CLI

Make sure you’re using the FastStore Platform CLI by installing the `@vtex/fsp-cli` package, which provides the necessary hooks and the basic structure for implementing the modules.

Learn more in the [FastStore Platform CLI](LINK) guide.

### Add the Analyzer to your project

To add the Analyzer to your project, run the following command:

```bash
pnpm add @vtex/fsp-analyzer
```

This will equip your project with the tools to maintain code quality and security standards throughout development.

### Understand the `hooks` folder

Your project's `hooks` folder allows you to add custom hooks to the development lifecycle. These hooks can be executed at different runtime stages, such as:

- `preBuild`: Runs before the build process.
- `postBuild`: Runs after the build process.
- `preDev`: Runs before the development server starts.
- `postDev`: Runs after the development server starts.

>ℹ Hooks are defined in the `src/hooks` folder and are executed according to the file name (Example: `pre.ts` will run before `post.ts`).

</Steps>

## Instructions

To ensure that the Analyzer runs as part of your build process and catches potential issues as early as possible, we recommend configuring the Analyzer in the `preBuild` hook. This hook allows the Analyzer to scan your code before the build starts, helping to detect and address issues early in the development cycle.

### Step 1 - Creating a pre-build hook

1. Open your FastStore project using the code editor of your choice.
2. Go to the `hooks/pre.tsx` file.
3. Add the following content:

  ```typescript
  import { FastStoreSandboxAnalyzer } from "@vtex/fsp-analyzer";

  export async function preBuild() {
    const analyzer = new FastStoreSandboxAnalyzer();

    try {
      await analyzer.analyzeFiles({
        filePattern: '{{your-module}}/**/*.{js,ts,jsx,tsx,css,less,scss}',
        cssOptions: {
          allowedNamespaces: ['extension-'],
          transformNonCompliant: true,
          defaultNamespace: 'extension-',
          verbose: true,
          overwriteTransformed: true,
        }
      });
    } catch (error) {
      console.error("Pre-build static analysis failed:", error);
      throw error;
    }
  }
  ```

  | Field | Type | Description |
  |:------|:-----|:------------|
  | `filePattern` | `string` | Glob pattern defining the files to be analyzed (example: `.{js,ts,jsx,tsx,css,less,scss}`). **Replace `{{your-module}}` according to your scenario.** |
  | `cssOptions` | `object` | Options for validating and transforming CSS namespace usage. |
  | &nbsp;&nbsp;├─`allowedNamespaces` | `string` | Array of allowed CSS namespace prefixes (example: `['extension-']`). Only selectors with these prefixes will be considered compliant. |
  | &nbsp;&nbsp;├─`transformNonCompliant` | `boolean` | If `true`, automatically updates non-compliant CSS selectors to match the expected namespace format. |
  | &nbsp;&nbsp;├─`defaultNamespace` | `string` | Default namespace prefix to selectors when auto-fixing non-compliant CSS (example: ` 'extension-'`. |
  | &nbsp;&nbsp;├─`verbose` | `boolean` | If `true`, provides detailed output and saves transformed files to disk. |
  | &nbsp;&nbsp;└─`overwriteTransformed` | `boolean` | If `true`, overwrites existing files with their transformed versions. |

Learn more about CSS options in the [CSS Analysis](LINK) guide.

### Step 2 - Executing static analysis

Register the hook in your project's entry point:

```typescript
export const hooks = {
  preBuild,
  // ... other hooks
};
```

Run your project:

```bash
pnpm run dev
```

Build your project:

```bash
pnpm run build
```

Once you finish these steps, you should see the Analyzer output in the console as shown in the example below:

![analyzer-output]()
