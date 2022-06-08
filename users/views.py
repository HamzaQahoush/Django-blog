from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # create form

from django.contrib import messages  # imported


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"account created for {username}")
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


"""
message types:
- message.debug
- message.info
- message.success
- message.warning
- message.error
"""
