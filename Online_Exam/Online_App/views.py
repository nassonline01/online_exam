from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
settings.AUTH_USER_MODEL
from Online_App.models import CustomUser
from django.contrib.auth import authenticate ,login ,logout

def Index(request):
    return render(request,'index.html')

def Register(request):
    if request.method =="POST":
        a = request.POST['firstname']
        b = request.POST['email']
        c = request.POST['username']
        d = request.POST['password']
        e = request.POST['usertype']
        f = User.objects.create_user(first_name=a,email=b,username=c,password=d,usertype_id=e)
        # f = CustomUser.objects.create_superuser(username="deni2002",password="deni2002",email="mariadeniston111@gmail.com",usertype_id=1)
        f.save()
        return HttpResponse("<script>window.alert('Saved Successfully');window.location.href='/log/';</script>")
    else:
        return render(request,'register.html')

def Login(request):
    if request.method=="POST":
        a = request.POST['username']
        b = request.POST['password']
        user = authenticate(request,username=a,password=b)
        if user is not None:
            login(request,user)
            return HttpResponse("<script>window.alert('Logined Successfully');window.location.href='/view/';</script>")
    else:
        return render(request,'login.html')
    
# def View(request):
#     try:
#         data = User.objects.get(username=request.user)
#     except:
#         ShowCounts()
#         return HttpResponse("<script>window.alert('Problem with username');</script>")
#     return render(request,'admin-dashboard.html',{'data':data})

# def ShowCounts(request):
#     Student_count = User.objects.filter(usertype_id=4).count()
#     Staff_count = User.objects.filter(usertype_id=2).count()
#     print("counts are",Student_count,Staff_count)
#     Details ={
#         'Student_count':1,
#         'Staff_count':2
#     }
#     # import pdb ; pdb.set_trace()
#     return render(request,'admin-dashboard.html',Details)

def View(request):
    try:
        # Fetch user data
        data = User.objects.get(username=request.user)

        # Fetch counts
        Student_count = User.objects.filter(usertype_id=4).count()
        Staff_count = User.objects.filter(usertype_id=2).count()
        
        print("Counts are:", Student_count, Staff_count,flush=True)
        
        # Pass both user details and counts to the template
        context = {
            'data': data,
            'Student_count': Student_count,
            'Staff_count': Staff_count
        }
    except User.DoesNotExist:
        return HttpResponse("<script>window.alert('Problem with username');</script>")

    return render(request, 'admin-dashboard.html', context)

def Logout(request):
    logout(request)
    return HttpResponse("<script>window.alert('Logged out Successfully');window.location.href='/reg/';</script>")
    