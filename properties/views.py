from django.shortcuts import render
import twilio.twiml

import twilio_api

def index(request):
    return render(request, 'properties/index.html')

def send_message(request):
    twilio_api.send_text_message()
    return render(request, 'properties/message_sent.html')

def cleaned(request):
    return render(request, 'properties/cleaned.html')
def sms(request):
	message = "";
	from_number = request.POST["From"]
	#return HttpResponse(from_number)
