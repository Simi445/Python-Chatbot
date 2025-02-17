# Python Chatbot

This project is a language model chatbot built using Django and the LangChain library. The chatbot can handle user queries, generate responses, and even generate images based on user prompts.

## Features

- Responds to user queries using a language model.
- Generates images based on user prompts.
- Maintains a chat history.
- Follows specific rules for answering questions and generating images.

## Installation
1. Download ollama on your PC:    https://ollama.com/download


2. Install the llama 3.1 version with 8B tokens:
   
   ```sh
   ollama run llama3.1
   ```
   
4. Clone the repository:

   ```sh
   git clone https://github.com/Simi445/Python-Chatbot.git
   cd Python-Chatbot
   ```

5. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

6. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

7. Run the Django server:
   
   ```sh
   python manage.py runserver
   ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Start interacting with the chatbot by typing your messages in the chat box.

## Showcase

![Chatbot](./chatbot.gif)

## Project Structure

- `src/page/LLM.py`: Contains the `LLMChatbot` class which handles the logic for generating responses and images.
- `src/page/views.py`: Contains the Django views for rendering the home page and handling chat interactions.
- `templates/index.html`: The HTML template for the chat interface.

## Code Documentation

### LLMChatbot Class

- `__init__(self)`: Initializes the chatbot with a specific model, time frame, context, and template.
- `download_image(self, prompt)`: Downloads an image based on the given prompt.
- `prompting_logic(self, prompt_text: str)`: Processes the user's prompt and generates a response.

### Views

- `home_view(request)`: Renders the home page with the current chat history.
- `chat_view(request)`: Handles the chat view, processing user messages and generating bot responses.

## Contributions

As part of my Python chatbot project, I integrated **Pollinations.AI** services to enhance its functionality with AI-generated text and images ([pollinations.ai](https://pollinations.ai/?utm_source=chatgpt.com)).

### Features Implemented:

- **Image Generation Integration**  
  Utilized **Pollinations.AI's image generation API** to allow the chatbot to generate and display images based on user prompts.

- **Text Generation Enhancement**  
  Integrated **Pollinations.AI's text generation API** to improve chatbot responses.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
