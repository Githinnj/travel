from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CEREDENTIALS")
            return redirect('login')


    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL TAKEN")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                print("USER CREATED")
                return redirect('login')

        else:
            messages.info(request,"PASSWORD NOT MATCHING")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')