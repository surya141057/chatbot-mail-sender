
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot.chatbot_logic import process_chat

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_msg = data.get('message', '')
        reply = process_chat(user_msg)
        return JsonResponse({'reply': reply})

    # For GET request, just render the template
    from django.shortcuts import render
    return render(request, 'chatbot/chatbot.html')
