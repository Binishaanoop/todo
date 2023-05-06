from django.shortcuts import render,redirect
from .models import User



# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def user_signup(request):
    msg=""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        #already exist email check
        user_exist = User.objects.filter(email = email).exists()
        if user_exist:
            msg="Email already exists!"
            return render(request, 'user/signup.html', {'status':msg})

        #create a new user
        user = User(name = name, email = email, mobile = mobile, password = password)
        user.save()
        msg = "your account has been created successfully"




    return render(request, 'user/signup.html',{'status':msg})


def user_login(request):
    msg=""
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email = name, password=password)
            return redirect('task:home')
        except:
            msg="invalid email or password"


    return render(request, 'user/login.html',{'status':msg})
