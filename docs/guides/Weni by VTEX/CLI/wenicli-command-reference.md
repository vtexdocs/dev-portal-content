# Weni CLI command reference

This documentation includes the default commands available in [Weni by VTEX CLI](weni-byvtex-guide.md).

## Default commands
Below is a brief description of the default commands available in Weni by VTEX CLI. For detailed information about each command, click on the respective command name. You can also get this information in your terminal by adding `--help` or `-h` after the command name.

| Command name | Description  |
| --- | --- |
| `weni` | Displays the main features and available commands directly in the terminal. |
| `weni --version` | Displays the current version of the Weni by VTEX CLI installed on your system. |
| `weni init` | Creates an initial setup ready for use and learning with Weni. |
| `weni login` | Authenticates with your Weni by VTEX platform account. |
| `weni project list` | Lists existing projects in your account. |
| `weni project list --org <org_uuid>` | Lists only projects from the specified organization UUID. |
| `weni project use [project_uuid]` | Sets the active project by providing its UUID. |
| `weni project current` | Identifies the project you are currently working with. |
| `weni project push [agent_definition_file] [--force-update]` | Deploys/updates your agents using the specified agent definition file. |
| `weni run [agent_definition_file] [agent_key] [tool_key] [-f FILE] [-v]` | Runs a specific tool from an agent locally. Specify a test file with `-f/--file`. If omitted, the CLI looks for `test_definition.yaml` in the tool folder. You can use `-v` to enable verbose logs. |
| `weni logs --agent <agent_key> --tool <tool_key> [--start-time ISO8601] [--end-time ISO8601] [--pattern TEXT]` | Fetches tool execution logs. Supports pagination and ISO 8601 date formats (e.g. `2024-01-01T00:00:00`). |