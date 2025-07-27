from langchain_core.messages import HumanMessage
from langchain_ollama import OllamaLLM
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

def get_available_models():
    """Get list of available Ollama models"""
    try:
        import subprocess
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[1:]  # Skip header
            models = []
            for line in lines:
                if line.strip():
                    model_name = line.split()[0]
                    models.append(model_name)
            return models
        else:
            print("Error: Could not get model list. Make sure Ollama is running.")
            return []
    except FileNotFoundError:
        print("Error: Ollama not found. Please install Ollama first.")
        return []

def main():
    print("🤖 Local AI Assistant (Ollama)")
    print("=" * 40)
    
    # Check if Ollama is available
    try:
        import subprocess
        subprocess.run(['ollama', '--version'], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("❌ Ollama not found or not running!")
        print("\nTo install Ollama:")
        print("1. Visit: https://ollama.ai/download")
        print("2. Download and install for your system")
        print("3. Start Ollama service")
        print("4. Download a model: ollama pull llama3.2")
        return
    
    # Get available models
    models = get_available_models()
    
    if not models:
        print("❌ No models found!")
        print("\nTo download a model, run:")
        print("ollama pull llama3.2")
        print("ollama pull mistral")
        print("ollama pull codellama")
        return
    
    # Let user choose model
    print(f"\nAvailable models: {', '.join(models)}")
    model_name = input(f"Enter model name (or press Enter for {models[0]}): ").strip()
    
    if not model_name:
        model_name = models[0]
    
    if model_name not in models:
        print(f"❌ Model '{model_name}' not found!")
        print(f"Available models: {', '.join(models)}")
        return
    
    # Create Ollama model
    try:
        model = OllamaLLM(
            model=model_name,
            temperature=0,
            base_url="http://localhost:11434"  # Default Ollama URL
        )
    except Exception as e:
        print(f"❌ Error connecting to Ollama: {e}")
        print("Make sure Ollama is running: ollama serve")
        return
    
    
    print(f"✅ Using {model_name}")
    print("Type 'quit' to exit, 'switch' to change models")
    print("-" * 40)
    
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            print("\nGoodbye!")
            break
        elif user_input.lower() == "switch":
            print("\n" + "=" * 40)
            models = get_available_models()
            if not models:
                print("❌ No models available!")
                continue
            
            print(f"Available models: {', '.join(models)}")
            model_name = input(f"Enter model name (or press Enter for {models[0]}): ").strip()
            
            if not model_name:
                model_name = models[0]
            
            if model_name not in models:
                print(f"❌ Model '{model_name}' not found!")
                continue
            
            try:
                model = OllamaLLM(
                    model=model_name,
                    temperature=0,
                    base_url="http://localhost:11434"
                )
                
                print(f"✅ Switched to {model_name}")
                print("-" * 40)
            except Exception as e:
                print(f"❌ Error switching models: {e}")
            continue

        print("\nAssistant: ", end="")
        try:
            response = model.invoke(user_input)
            print(response)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Try switching models with 'switch' command")

if __name__ == "__main__":
    main()
