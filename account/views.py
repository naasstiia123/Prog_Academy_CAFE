from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from main_page_cafe.views import Hero

def login_view(request):
    form = LoginForm(request.POST or None)
    next_get = request.GET.get('next')

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')

        return redirect(next_get or next_post or '/')
    hero = Hero.objects.filter(is_visible=True)

    return render(request, 'login.html', context={'form': form, 'hero': hero})

def logout_view(request):
    logout(request)
    return redirect('/')

def registration_view(request):
    user_form = RegistrationForm(request.POST or None)

    if user_form.is_valid():
        user = RegistrationForm(request.POST).save(commit=False)
        user.set_password(user_form.cleaned_data['password'])
        user.save()
        return render(request, 'registration_done.html', context={'user': user})

    hero = Hero.objects.filter(is_visible=True)
    return render(request, 'registration.html', context={'form': user_form, 'hero': hero})


