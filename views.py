from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .forms import RegisterForm



# Create your views here.
def index1 (request): 
    return render(request, 'main/index1.html')

def Course (request): 
    return render(request, 'main/Course.html')

def adminp (request): 
    return render(request, 'main/adminp.html')



def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form':form})


  
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'main/login.html', {})

def home(request):
    return render(request, 'main/home.html', {})

def logoutUser(request):
    logout(request)
    return redirect('index1')


   
def assign (request): 
    return render(request, 'main/assign.html')

def quiz (request): 
    return render(request, 'main/quiz.html')    

