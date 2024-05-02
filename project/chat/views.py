from django.shortcuts import render
from .models import *
from .forms import *

def pages(request):
    # message = request.POST.get('message')
    if request.method == 'POST':
        data = typing(request.POST)
        data.save()
    messages = chat_mesg.objects.all()
    return render(request, 'testChat.html', {'messages' : messages, 'lf' : typing})
# Create your views here.
