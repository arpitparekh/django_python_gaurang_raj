from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def show_register(request):

  if request.method=="POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      print("Form is valid")
      form.save()
      return redirect('login')
    else:
      print("Form is not valid")
      print(form.errors)
      return render(request, 'register.html',{'form': form})

  else:
    form = RegisterForm()
    return render(request, 'register.html',{'form': form})

def show_login(request):

  if request.method=="POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        print("Form is valid")
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')
        else:
          print("User is not authenticated")
          return redirect('login')

    else:
      print("Form is not valid")
      print("Form validation errors:", form.errors.as_data())
      return render(request, 'login.html',{'form': form})

  else:
    form = LoginForm(request=request)
    return render(request, 'login.html',{'form': form})


def show_home(request):
  return render(request, 'home_data.html')
