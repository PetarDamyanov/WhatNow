from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm
from users.models import Users, UsersType
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html', {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            dev_type = UsersType.objects.get(pk=1)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')

            new_user = Users(user=user, user_type=dev_type, phone=phone)
            new_user.save()

            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
