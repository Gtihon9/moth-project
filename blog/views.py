
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model



def default(request):
    return render(request, 'blog/base.html', {})

def register(request):
    messages = []
    if request.method == 'POST':

        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration//register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def getuserprofile(request, username):
    Users = get_user_model()
    User = Users.objects.filter(username=username).first()
    return render(request, 'blog/profile.html', {'User': User})

