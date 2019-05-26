from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required()
def user_dashboard(request):
    return render(request, 'dashboard.html')


def sign_in(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('user_dashboard')
            else:
                msg.append('You account has been deactivated!')
    else:
        msg.append('Invalid Login credentials, try again!')
    return render(request, 'login.html', {'errors': msg})

