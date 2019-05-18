from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('A new user has been successfully registered!')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

