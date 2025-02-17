from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
def loginUser(request):
    if request.method=='POST':
        # check if user  has enter correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # type: ignore
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutUser(request):            
    logout(request=request)
    return redirect('/login')