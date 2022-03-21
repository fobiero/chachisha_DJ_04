from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegForm

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, Your Account has been Created!')
            return redirect('login')
    else:
        form = UserRegForm()

    return render (request, 'register.html', {'form':form})

