from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm, UpdateImage, UpdateProfile

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
    if request.method == 'POST':
        u_prof = UpdateProfile(request.POST, instance=request.user)
        u_img = UpdateImage(request.POST,request.FILES, instance=request.user.profile)
        if u_prof.is_valid() and u_img.is_valid():
            u_prof.save()
            u_img.save()
            messages.success(request, f'Account Updated Successfully!')
            return redirect('profile')
    else:
        u_prof = UpdateProfile(instance=request.user)
        u_img = UpdateImage(request.user.profile)
    context = {
        'u_prof': u_prof,
        'u_img' : u_img
    }

    return render(request,'profile.html', context)


