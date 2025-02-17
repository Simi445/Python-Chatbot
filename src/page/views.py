from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from page.LLM import LLMChatbot
import json

# global chat history
chat_history = [("ai", "Hello! I am a language model chatbot, created by Simi, Sebi and Lau. How can I help you today?")]

# instantiate chatbot
chatbot = LLMChatbot()

def home_view(request):
    """
    Render the home page with the current chat history.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    context = {
        "chat_history": chat_history
    }
    return render(request, 'index.html', context)


@csrf_exempt
def chat_view(request):
    """
    Handle the chat view, processing user messages and generating bot responses.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Redirects to the home page after processing the chat.
    """
    if request.method == "POST":
        user_message = request.POST.get("message", "")

        if user_message:
            bot_response = chatbot.prompting_logic(user_message)

            chat_history.append(("user", user_message))
            chat_history.append(("ai", bot_response["text"]))

            if bot_response["image"]:
                chat_history.append(("ai_image", bot_response["image"]))

        return redirect('home')

    return redirect('home')