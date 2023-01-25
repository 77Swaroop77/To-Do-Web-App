from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from base.forms import TODOForms
from base.models import TODO
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='Login')
def Home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForms()
        todos = TODO.objects.filter(user=user)
        return render(request, 'index.html', context={'form': form, 'todos': todos})


def Login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'Login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('Home')
        else:
            context = {
                "form": form
            }
            return render(request, 'Login.html', context=context)


def SignUp(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('Login')
        else:
            return render(request, 'signup.html', context=context)


@login_required(login_url='Login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect('Home')
        else:
            return render(request, 'index.html', context={'form': form})


def delete_todo(request, id):
    print(id)
    TODO.objects.get(pk=id).delete()
    return redirect('Home')


def Signout(request):
    logout(request)
    return redirect('Login')
