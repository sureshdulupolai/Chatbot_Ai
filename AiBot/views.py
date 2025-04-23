from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai

# Create your views here.
@csrf_exempt
def AiHomePageFunction(request):
    genai.configure(api_key="AIzaSyAYvHy2v1jwGTCeaK-2Mw8vWchD8qY3NWs")
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    ai_response = None

    if request.method == 'POST':
        userData = request.POST.get('userData')

        if userData and userData.lower() not in ["exit", "quit", "bye"]:
            try:
                response = model.generate_content(userData)
                ai_response = response.text
            
            except Exception as e:
                ai_response = f"❌ Error: {str(e)}"
        else:
            ai_response = 'Thank Your Contact Us! Chat-Ai'

    return render(request, 'AiHome.html', {'ai_response': ai_response})
