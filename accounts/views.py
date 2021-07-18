from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not  None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credintals')
            return redirect("login")
    else:
        return render(request, 'accounts/login.html')

    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'].lower()
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #messages.info(request, 'Username Already Taken!')
                #return redirect('register')
                msg = ['Username Already Taken!']
                data = {}
                data['messages'] = msg
                data['email'] = email
                data['first_name'] = first_name
                data['last_name'] = last_name
                return render(request, 'accounts/register.html', data)
            elif User.objects.filter(email=email).exists():
                #messages.info(request, 'Email Already Taken!')
                #return redirect('register')
                msg = ['Email Already Taken!']
                data = {}
                data['messages'] = msg
                data['username'] = username
                data['first_name'] = first_name
                data['last_name'] = last_name
                return render(request, 'accounts/register.html', data)

            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                return redirect('login')
        else:
            # messages.info(request, 'Password Does Not Matched!')
            # print(messages)
            # return redirect('register')
            msg =[ 'Password Does Not Matched!']
            data ={}
            data['messages']=msg
            data['username'] = username
            data['email'] = email
            data['first_name'] = first_name
            data['last_name'] = last_name
            return render(request, 'accounts/register.html',data)
    else:
        return render(request, 'accounts/register.html')


def Logout(request):
    auth.logout(request)
    return redirect('/')
