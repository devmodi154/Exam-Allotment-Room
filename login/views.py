from django.shortcuts import render,redirect
from login.forms import UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_logout(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("user_login")

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('input1:input1_view')
            else:
            	print("HELLo1")
            	messages.error(request, "Invalid username or password.")
        else:
        	messages.error(request, "Invalid username or password.")
    else:
    	form = AuthenticationForm()
    return render(request = request,
                    template_name = "index.html",
                    context={"form":form})
