from django.shortcuts import render

# Create your views here.

def signup(request):
	return render(request,"accounts/signup.html")

def login(request):
	return render(request,"accounts/login.html")

def logout(request):
	return render(request,"accounts/logout.html")