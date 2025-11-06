---
title: "Weni by VTEX Guide"
slug: "weni-by-vtex-guide"
hidden: false
createdAt: "2025-10-23T17:08:52.219Z"
updatedAt: "2025-10-23T14:33:45.242Z"
excerpt: "Learn how to use Weni by VTEX CLI"
seeAlso:
 - "weni-by-vtex-cli"
hidePaginationPrevious: false
hidePaginationNext: false
---

Weni by VTEX CLI is a solution that helps you improve your customer service by using personalized AI-powered agents. This command-line tool simplifies the creation and management of multiple AI agents. Integrated with the Weni platform, it enables the development and deployment of high-performance agents across various communication channels, such as WhatsApp, Instagram, Facebook, and more.

With the CLI, you can:
- Create, deploy, and manage multiple AI agents
- Add custom tools to the agents
- Update agent configuration and behavior

> ⚠️ To use the Weni by VTEX CLI, you must have: a Weni Platform account; an account at [weni.ai](https://weni.ai/en); and at least one project in your account.

The content is organized as follows:
- [Installing the CLI](#installing-the-cli)
- 

## Installing the CLI

There are two installation methods:

- A [quick installation](#install-via-pip) with `pip`.
- A [manual installation](#install-via-poetry) with `Poetry`, for development purposes.

#### Install via pip

To install the CLI using `pip`, open the terminal and run the following command:

```bash
pip install weni-cli
```

#### Install via Poetry

To install the CLI manually, follow these steps:

1. Clone the repository by running the following command:

```bash
git clone https://github.com/weni-ai/weni-cli.git
cd weni-cli
```

2. Install dependencies and make the CLI executable by running the following command:

```bash
poetry shell
poetry install
```

### Verifying Installation

To verify that Weni CLI is installed, type the following command in your terminal:

```bash
weni
```

If the installation was successful, your terminal should display something like this:

![Weni Verification](weni-installation-verification.png)

## Troubleshooting

If you encounter any issues:

1. Check our [GitHub Issues](https://github.com/weni-ai/weni-cli/issues)
2. Create a new issue with:
   - Your operating system
   - Python version (`python --version`)
   - Error message
   - Steps to reproduce

#### Getting Started

To start your first agent, follow the steps below:

1. Open the terminal and run the following command:

```bash
weni login
```

This should open your browser on the login page for authentication. If that does not happen, you can open the URL shown in the terminal.

2. Log in using your Weni by VTEX account and password.
3. List your projects by running the following command:

```bash
weni project list
```

This will show all projects you have access to and, next to each of them, its universally unique identifier (UUID).

4. Select the project you want to work on by running the following command:

```bash
weni project use your-project-uuid
```

Replace `your-project-uuid` with the UUID from the project list.

5. To verify you're working on the correct project, you can run the following command:

```bash
weni project current
```

You will see the project's UUID in the terminal output.

6. To create an agent, run the following command:

```bash
weni init
```

This will:
- Create the necessary folder structure.
- Set up a pre-built CEP tool.
- Create a file named `agent_definition.yaml` with the configuration below. You can edit this at any point.

```bash
agents:
  sample_agent:
    name: "CEP Agent"
    description: "Weni's CEP agent"
    instructions:
      - "You are an expert in providing addresses to the user based on a postal code provided by the user"
      - "The user will send a ZIP code (postal code) and you must provide the address corresponding to this code."
    guardrails:
      - "Don't talk about politics, religion, or any other sensitive topic. Keep it neutral."
    tools:
      - get_address:
          name: "Get Address"
          source: 
            path: "tools/get_address"
            entrypoint: "main.GetAddress"
          description: "Function to get the address from the postal code"
          parameters:
            - cep:
                description: "postal code"
                type: "string"
                required: true
```

##### Understanding the source configuration
In the YAML above, there are two fields nested inside the `source` field:

- `path`: This field specifies the directory containing your tool implementation.
  - The command automatically creates a `tools` directory and a folder called `get_address` nested inside.
  - In this path, you can find the files `main.py`, `requirements.txt` and `test_definition.yaml`.

- `entrypoint`: This field informs the system which class to use.
  - Using `main.GetAddress` determines that the system finds the file named `main.py`, uses the `GetAddress` class inside of the file and that the calss must inherit from the `tools` base class.

Your project structure should look like this:

```
my-agent-project/
├── agent_definition.yaml
└── tools/
    └── get_address/
        ├── main.py             # Contains GetAddress class
        └── requirements.txt    # Dependencies
```

If the command doesn't work, you can implement this tool manually following the next steps:

6.1 Create the tool directory

```bash
   mkdir -p tools/get_address
   cd tools/get_address
```

6.2 Create the file `tools/get_address/main.py` and insert the following: 

```python
   from weni import Tool
   from weni.context import Context
   from weni.responses import TextResponse
   import requests


   class GetAddress(Tool):
       def execute(self, context: Context) -> TextResponse:
           cep = context.parameters.get("cep", "")
           address_response = self.get_address_by_cep(cep=cep)
           return TextResponse(data=address_response)

       def get_address_by_cep(self, cep):
           url = f"https://viacep.com.br/ws/{cep}/json/"
           response = requests.get(url)
           return response.json()
```

- The class name `GetAddress` must match the class name in the entrypoint
- The file name `main.py` must match the file name in the entrypoint
- The class must inherit from `Tool` and implement the `execute` method

6.3 Create the `requirements.txt` file

```txt
   requests==2.32.3
```

If you have credentials and global files, place these files in `tools/get_address` during local runs:

```ini
# .env
api_key=your-development-api-key
```

```ini
# .globals
BASE_URL=https://api.example.com
```

7. **(Optional) Add credentials and globals files**

Place these files in `tools/get_address/` if needed during local runs:

```ini
# .env
api_key=your-development-api-key
```

```ini
# .globals
BASE_URL=https://api.example.com
```

8. Deploy Agent

```bash
weni project push agent_definition.yaml
```

#### Advanced Configuration

##### Custom Parameters

You can add more parameters to your tools:

```yaml
parameters:
  - format:
      description: "Response format (json or text)"
      type: "string"
      required: false
      default: "json"
```

##### Multiple Tools

Agents can have multiple tools:

```yaml
tools:
  - get_address:
      # tool definition
  - validate_cep:
      # another tool definition
```