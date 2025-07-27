# Local AI Assistant (Ollama)

A Python-based local AI assistant that uses Ollama to run large language models locally on your machine.

## Features

- 🤖 **Local AI Models**: Run AI models locally using Ollama
- 🔄 **Model Switching**: Switch between different models during conversation
- 💬 **Interactive Chat**: Simple command-line interface for chatting with AI
- 🔒 **Privacy**: All conversations stay on your local machine
- ⚡ **Fast**: No internet dependency for responses

## Prerequisites

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running
3. **uv** package manager (recommended) or pip

## Installation

1. **Install Ollama**:
   - Visit [https://ollama.ai/download](https://ollama.ai/download)
   - Download and install for your system
   - Start Ollama service: `ollama serve`

2. **Clone this repository**:
   ```bash
   git clone <your-repo-url>
   cd llm_project
   ```

3. **Install dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. **Download a model**:
   ```bash
   ollama pull *name of model*

   # For example
   ollama pull llama3.2:latest
   ```
   Visit [https://ollama.com/search](https://ollama.com/search) to find which model you would like to locally download.

## Usage

Run the assistant:
```bash
uv run main.py
```

### Available Commands

- **Type your message**: Chat with the AI
- **`quit`**: Exit the application
- **`switch`**: Switch to a different model

### Example Session

```
🤖 Local AI Assistant (Ollama)
========================================
Available models: llama3.2:latest, gemma:latest
Enter model name (or press Enter for llama3.2:latest): 

✅ Using llama3.2:latest
Type 'quit' to exit, 'switch' to change models
----------------------------------------
You: What's 9 + 10?
Assistant: 9 + 10 = 19
You: quit
Goodbye!
```

## Supported Models

Any model available in Ollama can be used. Popular options include:

- `llama3.2` - Meta's Llama 3.2 model
- `gemma` - Google's Gemma model
- `mistral` - Mistral AI's model
- `codellama` - Code-focused Llama variant

## Project Structure

```
llm_project/
├── main.py              # Main application file
├── pyproject.toml       # Project dependencies and configuration
├── README.md           # This file
├── .gitignore          # Git ignore rules
└── .venv/              # Virtual environment (not committed)
```

## Dependencies

- `langchain-core` - Core LangChain functionality
- `langchain-ollama` - Ollama integration for LangChain
- `python-dotenv` - Environment variable management

## Troubleshooting

### "Ollama not found" error
- Make sure Ollama is installed and running
- Run `ollama serve` to start the service

### "No models found" error
- Download a model: `ollama pull llama3.2`
- Check available models: `ollama list`

### Import errors
- Make sure you're using `uv run main.py` or have activated the virtual environment
- Reinstall dependencies: `uv sync`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
