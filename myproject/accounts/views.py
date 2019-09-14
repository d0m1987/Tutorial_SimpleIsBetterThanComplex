from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})