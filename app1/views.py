from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        user=User.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,'User Already Exist')
            return redirect('/register/')
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Register Success")
    form=RegisterForm()
    return render(request,'register.html',{'form':form})


