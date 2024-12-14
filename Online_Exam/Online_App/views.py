from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth.models import User

def Index(request):
    return render(request,'index.html')

def Register(request):
    if request.method =="POST":
        a = request.POST['firstname']
        c = request.POST['email']
        d = request.POST['username']
        e = request.POST['password']
        f = User.objects.create_user(first_name=a,email=c,username=d,password=e)
        f.save()
        return HttpResponse("<script>window.alert('Saved Successfully');window.location.href='/log/';</script>")
    else:
        return render(request,'register.html')

def Login(request):
    return render(request,'login.html')