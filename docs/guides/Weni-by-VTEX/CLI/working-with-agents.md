---
title: "Working with agents"
slug: "working-with-agents"
hidden: false
createdAt: "2025-11-06T13:05:20.961Z"
updatedAt: "2025-11-06T13:05:57.445Z"
excerpt: "Learn how to create, configure, and deploy agents using the Weni by VTEX CLI, with some examples of agents."
---

# Working with Agents

Learn how to create, configure, and deploy AI agents using Weni by VTEX CLI.

## Agent Definition File

Agents are defined using YAML files. Here's the basic structure:

```yaml
agents:
   agent_id:
      name: "Agent Name"
      description: "Agent Description"
      instructions:
         - "Instruction 1"
         - "Instruction 2"
      guardrails:
         - "Guardrail 1"
      tools:
         - tool_name:
            name: "Tool Name"
            source:
               path: "tools/tool_name"
               entrypoint: "main.ToolClass"
            description: "Tool Description"
            parameters:
               - param_name:
                  description: "Parameter Description"
                  type: "string"
                  required: true
                  contact_field: true
```

### Key Components

1. **Agent ID**
   - Unique identifier for your agent
   - Used internally by the system

2. **Basic Information**
   - `name`: Display name (max 55 characters)
   - `description`: Brief description of the agent's purpose

3. **Instructions**
   - Guide the agent's behavior
   - Minimum 40 characters each
   - Should be clear and specific

4. **Guardrails**
   - Define boundaries and limitations
   - Prevent unwanted behavior

5. **Tools**
   - Custom functionalities
   - Implemented as Python classes using the Weni by VTEX SDK

### Tool Source Configuration

The `source` field is critical for locating and executing your tool:

```yaml
source:
  path: "tools/tool_name"
  entrypoint: "main.ToolClass"
```

- **path**: Points to the directory containing your tool implementation
  - Example: `tools/get_address` refers to a folder named `get_address` inside a `tools` directory
  - This folder should contain your Python modules and requirements.txt

- **entrypoint**: Specifies which class to use in which file
  - Format: `filename.ClassName`
  - Example: `main.GetAddress` means:
    - Look for a file named `main.py` in the path directory
    - Find a class named `GetAddress` inside that file
    - This class must inherit from the `Tool` class

Your directory structure should look like:
```
project/
├── agents.yaml
└── tools/
    └── get_address/
        ├── main.py             # Contains GetAddress class
        └── requirements.txt    # Dependencies
```

## Creating Tools

### Tool Implementation Structure

```python
from weni import Tool
from weni.context import Context
from weni.responses import TextResponse

class ToolName(Tool):
    def execute(self, context: Context) -> TextResponse:
        # Extract parameters
        parameters = context.parameters
        param_value = parameters.get("param_name", "")
        
        # Process the request
        result = self.process_request(param_value)
        
        # Return response
        return TextResponse(data=result)
        
    def process_request(self, param_value):
        # Your business logic here
        return {"key": "value"}
```

#### Important Requirements
- The class **must** inherit from `Tool`
- The class **must** implement the `execute` method
- The class name **must** match the class name in your entrypoint

## Deploying Agents

### Push Command

Deploy your agent using:

```bash
weni project push agents.yaml
```

The command:
1. Validates your YAML
2. Uploads tools
3. Creates/updates the agent

### Deployment Best Practices

1. **Version Control**
   - Keep agent definitions in version control
   - Document changes

2. **Testing**
   - Test locally when possible
   - Start with staging environment
   - Verify all tools work

3. **Organization**
   - Use clear file names
   - Keep related files together
   - Document dependencies

## Advanced Topics

### Parameter Types

Available parameter types:
- `string`
- `number`
- `integer`
- `boolean`
- `array`

### Response Formats

Tools can return:
- Text responses via `TextResponse`
- Structured data 
- Error messages

### Error Handling

Your tools should:
1. Validate inputs
2. Handle exceptions gracefully
3. Return meaningful error messages

## Troubleshooting

### Common Issues

1. **Deployment Failures**
   - Check YAML syntax
   - Verify tool paths
   - Confirm project selection

2. **Tool Errors**
   - Verify tool entrypoint (class name)
   - Test tool class locally
   - Check parameter handling in context
   - Verify API endpoints

3. **Agent Behavior**
   - Review instructions
   - Check guardrails
   - Test with various inputs

### Best Practices

1. **Development Flow**
   - Develop locally
   - Test in staging
   - Deploy to production

2. **Monitoring**
   - Keep deployment logs
   - Monitor tool performance
   - Track user interactions

3. **Updates**
   - Plan changes carefully
   - Test updates thoroughly
   - Document modifications

# Agent Examples

Here are some examples of agents you can use.

- [Book Agent](#book-agent): Searches for book information, including title, author, description, and other details.
- [CEP Agent](#cep-agent): Provides an address based on its Brazilian postal code.
- [Movie Agent](#movie-agent): Searches for movie information, with automatic translation of titles and descriptions.
- [News Agent](#news-agent): Retrieves up-to-date news about various topics through a news API.

## Book Agent

This example shows how to create an agent that provides detailed information about books based on the title provided by the user.

### Agent Definition

Create a file called `agent_definition.yaml`:

```yaml
agents:
    book_agent:
      name: "Book Agent"
      description: "Expert in searching for book information"
      instructions:
        - "You are an expert in searching for detailed information about books"
        - "When the user asks about a book, you should search and present the most relevant information"
        - "The API returns information in English, and you should translate the description to Portuguese naturally and fluently"
        - "If you can't find the book, suggest similar titles"
        - "When translating the description, maintain the tone and style of the original text, adapting only to Brazilian Portuguese"
        - "Provide information about authors, publisher, publication date, page count, and ratings when available"
        - "You must translate the book description to Portuguese before presenting it to the user"
      guardrails:
        - "Maintain a professional and informative tone when presenting books"
        - "Don't make assumptions about book content"
        - "Provide accurate and verified information"
        - "When translating, maintain fidelity to the original text meaning"
        - "Mention when rating or page count information is not available"
      tools:
      - get_books:
          name: "Search Books"
          source:
            path: "tools/get_books"
            entrypoint: "books.GetBooks"
            path_test: "test_definition.yaml"
          description: "Function to search for book information"
          parameters:
            - book_title:
                description: "book title to search for"
                type: "string"
                required: true
                contact_field: true
```

### Tool Implementation

Create a file `tools/get_books/books.py`:

```python
from weni import Tool
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime


class GetBooks(Tool):
    def execute(self, context: Context) -> TextResponse:
        apiKey = context.credentials.get("apiKey")
        
        book_title = context.parameters.get("book_title", "")
        books_response = self.get_books_by_title(title=book_title)

        # Format the response
        items = books_response.get("items", [])
        if not items:
            return TextResponse(data="Sorry, I couldn't find information about this book.")
        
        response_data = {
            "status": "success",
            "totalResults": len(items[:5]),
            "books": []
        }
        
        for book in items[:5]:
            volume_info = book.get("volumeInfo", {})
            book_data = {
                "id": book.get("id"),
                "title": volume_info.get("title"),
                "authors": volume_info.get("authors", []),
                "publisher": volume_info.get("publisher"),
                "publishedDate": volume_info.get("publishedDate"),
                "description": volume_info.get("description", ""),
                "pageCount": volume_info.get("pageCount"),
                "categories": volume_info.get("categories", []),
                "averageRating": volume_info.get("averageRating"),
                "ratingsCount": volume_info.get("ratingsCount"),
                "imageLinks": volume_info.get("imageLinks", {}),
                "language": volume_info.get("language"),
                "previewLink": volume_info.get("previewLink"),
                "infoLink": volume_info.get("infoLink")
            }
            response_data["books"].append(book_data)
            
        return TextResponse(data=response_data)

    def get_books_by_title(self, title):
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": title
        }
        response = requests.get(url, params=params)
        return response.json()
```

Create a file `tools/get_books/requirements.txt`:

```
requests==2.32.3
```

Create a file `tools/get_books/test_definition.yaml`:

```yaml
tests:
    test_1:
        parameters:
            book_title: "The Hobbit"
```

### Testing the Tool Locally

Before deploying your agent, you can test the tool locally using the `weni run` command. This allows you to verify that your tool works correctly and debug any issues.

To test the Book Agent tool:

```bash
weni run agent_definition.yaml book_agent get_books
```

This command will execute the tests defined in the `test_definition.yaml` file and show you the output. You should see the book information for "The Hobbit" test case.

If you need more detailed logs for debugging, you can add the `-v` flag:

```bash
weni run agent_definition.yaml book_agent get_books -v
```

The verbose output will show you more details about the execution process, helping you identify and fix any issues with your tool.

### Deployment Steps

1. Deploy the agent:
   ```bash
   weni project push agent_definition.yaml
   ```

### Testing

After deployment, you can test the agent:

1. Open your project in the Weni by VTEX platform
2. Find the Book Agent in your agents list
3. Start a conversation
4. Send a book title (e.g., "Pride and Prejudice" or "Harry Potter")

The agent will respond with detailed information about the book, including title, authors, publisher, publication date, page count, and ratings when available. The book description will be automatically translated to Portuguese. 

## CEP Agent

This example shows how to create an agent that can provide address information based on Brazilian postal codes (CEP).

### Agent Definition

Create a file named `agents.yaml`:

```yaml
agents:
  sample_agent:
    name: "CEP Agent"
    description: "Weni's CEP agent"
    instructions:
      - "You are an expert in providing addresses to the user based on a postal code provided by the user"
      - "The user will send a ZIP code (postal code) and you must provide the address corresponding to this code."
    guardrails:
      - "Don't talk about politics, religion or any other sensitive topic. Keep it neutral."
    tools:
      - get_address:
          name: "Get Address"
          source: 
            path: "tools/get_address"
            entrypoint: "main.GetAddress"
            path_test: "test_definition.yaml"
          description: "Function to get the address from the postal code"
          parameters:
            - cep:
                description: "postal code of a place"
                type: "string"
                required: true
                contact_field: true
```

### Tool Implementation

Create a file `tools/get_address/main.py`:

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

Create a file `tools/get_address/requirements.txt`:

```
requests==2.31.0
```

Create a file `tools/get_address/test_definition.yaml`:

```yaml
tests:
    test_1:
        parameters:
            cep: "01311-000"
    test_2:
        parameters:
            cep: "70150-900"
    test_3:
        parameters:
            cep: "20050-090"
```

### Testing the Tool Locally

Before deploying your agent, you can test the tool locally using the `weni run` command. This allows you to verify that your tool works correctly and debug any issues.

To test the CEP Agent tool:

```bash
weni run agent_definition.yaml cep_agent get_address
```

This command will execute the tests defined in the `test_definition.yaml` file and show you the output. You should see the address information for the Brazilian postal codes specified in the test cases.

If you need more detailed logs for debugging, you can add the `-v` flag:

```bash
weni run agent_definition.yaml cep_agent get_address -v
```

This will run the test cases defined in `test_definition.yaml` and show you the output, helping you identify and fix any issues with your tool.

### Deployment Steps

1. Deploy the agent:
   ```bash
   weni project push agents.yaml
   ```

### Testing

After deployment, you can test the agent by:

1. Opening your project in the Weni by VTEX platform
2. Finding the CEP Agent in your agents list
3. Starting a conversation
4. Sending a valid Brazilian postal code (e.g., "01311-000")

## Movie Agent

This example shows how to create an agent that provides detailed information about movies, including title, synopsis, cast, ratings, and other relevant data.

### Agent Definition

Create a file called `agent_definition.yaml`:

```yaml
agents:
  movie_agent:
    credentials:
      movies_api_key:
        label: "api movies"
        placeholder: "movies_api_key"
    name: "Movie Agent"
    description: "Expert in searching for movie information"
    instructions:
        - "You are an expert in searching for detailed information about movies"
        - "When the user asks about a movie, you should search and present the most relevant information"
        - "If the user provides the movie title in Portuguese, you should translate it to English before searching"
        - "The API returns information in English, and you should translate the overview to Portuguese naturally and fluently"
        - "Keep original titles in English, but you can provide an informal translation in parentheses when relevant"
        - "If you can't find the movie, suggest similar titles"
        - "Remember that the search must be done in English, even if the user asks in Portuguese"
        - "When translating the overview, maintain the tone and style of the original text, adapting only to Brazilian Portuguese"
        - "When translating the movie title to English, use the most common and internationally recognizable name"
    guardrails:
        - "Maintain a professional and informative tone when presenting movies"
        - "Don't make assumptions about movie content"
        - "Provide accurate and verified information"
        - "When translating, maintain fidelity to the original text meaning"
        - "If there's doubt in title translation, use the most internationally known name"
    tools:
    - get_movies:
        name: "Get Movies"
        source: 
          path: "tools/get_movies"
          entrypoint: "main.GetMovies"
          path_test: "test_definition.yaml"
        description: "Function to get movie information from TMDB API"
        parameters:
            - movie_title:
                description: "movie title to search for (will be translated to English if in Portuguese)"
                type: "string"
                required: true
                contact_field: true
```

### Tool Implementation

Create a file `tools/get_movies/main.py`:

```python
from weni import Tool
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime

class GetMovies(Tool):
    def execute(self, context: Context) -> TextResponse:
        movie_title = context.parameters.get("movie_title", "")
        api_key = context.credentials.get("movies_api_key")
        
        # Search for movies by title
        movies_response = self.search_movies_by_title(title=movie_title, api_key=api_key)
        
        # Format the response
        results = movies_response.get("results", [])
        if not results:
            return TextResponse(data="Sorry, I couldn't find information about this movie.")
        
        # Get the first (most relevant) movie
        movie_id = results[0].get("id")
        
        # Get detailed information about the movie
        movie_details = self.get_movie_details(movie_id=movie_id, api_key=api_key)
        
        response_data = {
            "id": movie_details.get("id"),
            "title": movie_details.get("title"),
            "original_title": movie_details.get("original_title"),
            "tagline": movie_details.get("tagline"),
            "overview": movie_details.get("overview"),
            "release_date": movie_details.get("release_date"),
            "runtime": movie_details.get("runtime"),
            "vote_average": movie_details.get("vote_average"),
            "vote_count": movie_details.get("vote_count"),
            "genres": movie_details.get("genres", []),
            "poster_path": f"https://image.tmdb.org/t/p/w500{movie_details.get('poster_path')}" if movie_details.get("poster_path") else None,
            "backdrop_path": f"https://image.tmdb.org/t/p/original{movie_details.get('backdrop_path')}" if movie_details.get("backdrop_path") else None
        }
        
        return TextResponse(data=response_data)

    def search_movies_by_title(self, title, api_key):
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": title,
            "language": "en-US",
            "page": 1
        }
        response = requests.get(url, params=params)
        return response.json()
        
    def get_movie_details(self, movie_id, api_key):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": api_key,
            "language": "en-US",
            "append_to_response": "credits,similar"
        }
        response = requests.get(url, params=params)
        return response.json()
```

Create a file `tools/get_movies/requirements.txt`:

```
requests==2.32.3
```

Create a file `tools/get_movies/test_definition.yaml`:

```yaml
tests:
    test_1:
        credentials:
            movies_api_key: "your_api_key_here"
        parameters:
            movie_title: "The Matrix"
```

### Getting Credentials

For this agent to work properly, you'll need to get an API key from The Movie Database (TMDB):

1. Visit the [TMDB](https://www.themoviedb.org/) website
2. Register for a free account
3. Access the API section in your account and request an API key
4. Copy your API key
5. When deploying the agent, you'll need to provide this key as a credential

### Testing the Tool Locally

Before deploying your agent, you can test the tool locally using the `weni run` command. This allows you to verify that your tool works correctly and debug any issues.

Since this tool requires credentials, create a `.env` file in the tool folder with your TMDB API key (e.g., `tools/get_movies/.env`):

```
movies_api_key=your_actual_tmdb_api_key_here
```

To test the Movie Agent tool:

```bash
weni run agent_definition.yaml movie_agent get_movies
```

This command will execute the tests defined in the `test_definition.yaml` file and show you the output. The CLI will automatically pick up the credentials from the tool folder `.env` file and make them available to your tool during execution.

If you need more detailed logs for debugging, you can add the `-v` flag:

```bash
weni run agent_definition.yaml movie_agent get_movies -v
```

The verbose output will show you more details about the execution process, including API requests and responses, helping you identify and fix any issues with your tool.

### Deployment Steps

1. Deploy the agent:
   ```bash
   weni project push agent_definition.yaml
   ```

### Testing

After deployment, you can test the agent:

1. Open your project in the Weni by VTEX platform
2. Find the Movie Agent in your agents list
3. Provide the TMDB API key in the credential settings
4. Start a conversation
5. Send a movie title in Portuguese or English (e.g., "The Godfather" or "Pulp Fiction")

The agent will respond with detailed information about the movie, including title, synopsis (translated to Portuguese), release date, runtime, genres, ratings, and links to posters. If the title is provided in Portuguese, the agent will automatically translate it to perform the search. 

## News Agent

This example shows how to create an agent that provides up-to-date news on various topics through a news API.

### Agent Definition

Create a file called `agent_definition.yaml`:

```yaml
agents:
    news_agent:
        credentials:
            apiKey:
                label: "API Key"
                placeholder: "apiKey"
        name: "News Agent"
        description: "Expert in searching and providing news about any topic"
        instructions:
            - "You are an expert in searching and providing updated news about any topic"
            - "When the user asks about a topic, you should search and present the most relevant news"
            - "Always be helpful and provide brief context about the news found"
            - "If you can't find news about the topic, suggest related topics"
            - "Always use english to answer the user and be polite"
        guardrails:
            - "Maintain a professional and impartial tone when presenting news"
            - "Don't make assumptions or speculations about the news"
            - "Avoid sharing sensationalist or unverified news"
        tools:
        - get_news:
            name: "Get News"
            source:
                path: "tools/get_news"
                entrypoint: "main.GetNews"
                path_test: "test_definition.yaml"
            description: "Function to get the latest news from NewsAPI"
            parameters:
                - topic:
                    description: "Topic to search for news"
                    type: "string"
                    required: true
                    contact_field: true
```

### Tool Implementation

Create a file `tools/get_news/main.py`:

```python
from weni import Tool
from weni.context import Context
from weni.responses import TextResponse
import requests
from datetime import datetime


class GetNews(Tool):
    def execute(self, context: Context) -> TextResponse:
        apiKey = context.credentials.get("apiKey")
        
        topic = context.parameters.get("topic", "")
        news_response = self.get_news_by_topic(topic=topic, apiKey=apiKey)
        
        # Format the response
        articles = news_response.get("articles", [])
        if not articles:
            return TextResponse(data="Sorry, I couldn't find any news on this topic.")
        
        response_data = {
            "status": news_response.get("status"),
            "totalResults": len(articles[:10]),
            "articles": []
        }
        
        # Get only the first 10 articles
        for article in articles[:10]:
            article_data = {
                "source": article.get("source", {}),
                "author": article.get("author"),
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "urlToImage": article.get("urlToImage"),
                "publishedAt": article.get("publishedAt"),
                "content": article.get("content")
            }
            response_data["articles"].append(article_data)
            
        return TextResponse(data=response_data)

    def get_news_by_topic(self, topic, apiKey):
        url = f"https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "sortBy": "popularity",
            "apiKey": apiKey,
            "language": "en"
        }
        response = requests.get(url, params=params)
        return response.json()
```

Create a file `tools/get_news/requirements.txt`:

```
requests==2.32.3
```

Create a file `tools/get_news/test_definition.yaml`:

```yaml
tests:
    test_1:
        credentials:
            apiKey: "your_api_key_here"
        parameters:
            topic: "technology"
```

### Getting Credentials

For this agent to work properly, you'll need to get an API key from News API:

1. Visit the [News API](https://newsapi.org/) website
2. Register for a free account
3. Copy your API key from your account
4. When deploying the agent, you'll need to provide this key as a credential

### Testing the Tool Locally

Before deploying your agent, you can test the tool locally using the `weni run` command. This allows you to verify that your tool works correctly and debug any issues.

Since this tool requires credentials, create a `.env` file in the tool folder with your API key (e.g., `tools/get_news/.env`):

```
apiKey=your_actual_news_api_key_here
```

To test the News Agent tool:

```bash
weni run agent_definition.yaml news_agent get_news
```

This command will execute the tests defined in the `test_definition.yaml` file and show you the output. The CLI will automatically pick up the credentials from the tool folder `.env` file and make them available to your tool during execution.

If you need more detailed logs for debugging, you can add the `-v` flag:

```bash
weni run agent_definition.yaml news_agent get_news -v
```

The verbose output will show you more details about the execution process, helping you identify and fix any issues with your tool.

### Deployment Steps

1. Deploy the agent:
   ```bash
   weni project push agent_definition.yaml
   ```

### Testing

After deployment, you can test the agent:

1. Open your project in the Weni by VTEX platform
2. Find the News Agent in your agents list
3. Provide the News API key in the credential settings
4. Start a conversation
5. Send a topic to search for news (e.g., "technology", "sports", "business")

The agent will respond with the most relevant news about the requested topic, including title, description, source, author, publication date, and links to the full article. 
