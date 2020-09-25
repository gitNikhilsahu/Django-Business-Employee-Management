from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .form import *

def employee_login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Employee.objects.get(user=user)
                return redirect('/employee/{}/edit'.format(user.id))
            except:
                return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    form = EmployeeFormLogin()
    context = {"form": form}
    return render(request, 'employee/employee_login.html', context)

def employee_register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Employee.objects.create(user=user,)
            messages.success(request, 'Account was created for ' + username)
            return redirect('/employee/login')
    context ={'form': form}
    return render(request, 'employee/employee_register.html', context)

# def employee_profile_update_view(request):
#     context = {}
#     if request.POST:
#         form = EmployeeForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             context['form'] = form
#     else:
#         form = EmployeeForm()
#         context['form'] = form
#     return render(request, 'employee/employee_register.html', context)

def employee_logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    logout(request)
    return redirect('/employee/login')

def employee_edit_view(request,id):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    context = {}
    employee = Employee.objects.get(user=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance = employee)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Not Valid')
    else:
        context['form'] = form
    return render(request, 'employee/employee_edit.html', context)

def employee_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    employee = Employee.objects.get(user=id)
    employee.delete()
    return redirect("/")