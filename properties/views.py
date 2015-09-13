from django.shortcuts import render
from .models import Tennant
import twilio_api

def index(request):
    return render(request, 'properties/index.html')

def send_message(request):
    twilio_api.send_text_message()
    return render(request, 'properties/message_sent.html')

def cleaned(request):
    return render(request, 'properties/cleaned.html')

def sms(request):
	pass

def check(request):
	responded = Tennant.objects.all()[0].responded
	context = {'responded': responded}
	return render(request, 'properties/check.html', context)

def reset(request):
	tennant = Tennant.objects.all()[0]
	tennant.responded = False
	tennant.save()
	return render(request, 'properties/index.html')
