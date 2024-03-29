from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import emp
# Create your views here.


def home(request):
    emps = emp.objects.all()

    
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate 
        user = authenticate(request,username=username,password=password)
        
        if user is not None :
            login(request,user)
            messages.success(request,"You have been logged In")
            return redirect('home')
        else:
            messages.success(request,"Wrong crendtials , please try agian !!")
        
    return render(request,'home.html',{
        'emps':emps,
    })
       

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')
    

@login_required
def user_registration(request):
    
    return render(request,'registration.html',{
        
    })
    