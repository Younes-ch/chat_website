from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.

def home_screen_view(request):
    return render(request, 'core/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'core/signup.html', context)
        
    form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required(login_url='login')
def logout_view(request):
        logout(request)
        return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Username OR Passowrd does not exists.'})
    
    return render(request, 'core/login.html')

def rooms_view(request):
     pass

