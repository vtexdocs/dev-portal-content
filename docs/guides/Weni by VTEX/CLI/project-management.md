# Project Management

Learn how to manage your Weni projects using the CLI.

## Project Commands

### List Projects

View all projects you have access to:

```bash
weni project list
```

Filter projects by organization UUID:

```bash
weni project list --org <org-uuid>
```

If many results are available, you'll be prompted to load more pages (`p`) or quit (`q`).

This command shows:
- Project UUID
- Project name
- Organization
- Creation date

### Select Project

Set a project as your current working project:

```bash
weni project use <project-uuid>
```

Replace `<project-uuid>` with the UUID from the project list.

### View Current Project

Check which project you're currently working with:

```bash
weni project current
```

This prints the current project UUID stored by the CLI, e.g.: `Current project: <uuid>`

## Project Context

The CLI maintains a "current project" context, which is used by other commands like `project push`. This context is stored in your `.weni_cli` file.

### Why Project Context Matters

- Simplifies command usage (no need to specify project in every command)
- Prevents accidental deployments to wrong projects
- Maintains consistent workflow

## Best Practices

### Project Organization

1. **Naming Conventions**
   - Use clear, descriptive project names
   - Follow your organization's naming standards

2. **Project Structure**
   - Keep related agents together
   - Maintain consistent file organization

### Working with Multiple Projects

1. **Context Switching**
   - Always verify current project before operations
   - Use `project current` to confirm active project

2. **Project Isolation**
   - Keep project-specific files in separate directories
   - Use version control for project configurations

## Common Workflows

### Starting a New Project

1. Create project in Weni platform
2. List projects to get UUID:
   ```bash
   weni project list
   ```
3. Select the new project:
   ```bash
   weni project use <new-project-uuid>
   ```
4. Verify selection:
   ```bash
   weni project current
   ```

### Managing Multiple Projects

1. List available projects
2. Switch between projects as needed
3. Verify current project before operations
4. Keep project files organized

## Troubleshooting

### Common Issues

1. **Project Not Found**
   - Verify project UUID
   - Check your access permissions
   - Ensure you're in the correct environment

2. **Unable to Switch Projects**
   - Verify `.weni_cli` file permissions
   - Check authentication status
   - Confirm project exists and is accessible

3. **Project List Empty**
   - Verify authentication
   - Check environment configuration
   - Confirm you have project access

### Getting Help

If you encounter issues:
1. Check command syntax
2. Verify project access
3. Contact support if needed