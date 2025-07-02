from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello guys my name is Kedar Bhame")
    return render(request,'website/index.html')

def contact(request):
    # return HttpResponse("You are in the contact page.")
    return render(request,'website/contact.html')