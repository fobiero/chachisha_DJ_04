from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm

# @TODO:registrer page 
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

# @TODO:get user credentials 
@login_required
def profile(request):

    return render(request,'profile.html')


