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

  if request.session.get('isLogin'):
    return redirect('home')

  if request.method=="POST":
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        print("Form is valid")
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          request.session['isLogin'] = True
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


def show_session(request):
  # cretae a session
  # request.session['name'] = 'John'
  # request.session['age'] = 25

  print(request.session.get('name'))
  print(request.session.get('age'))

  return render(request, 'session_dis.html')


def show_logout(request):
  # request.session.flush()
  request.session['isLogin'] = False
  return redirect('login')
