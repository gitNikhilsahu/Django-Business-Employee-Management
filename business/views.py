from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *
from employee.models import *
from .form import *

def business_list_view(request):
    if not request.user.is_authenticated:
        return redirect('/employee/login')

    business = Business.objects.all()
    total_profit_month = 0
    data = ProfitModel.objects.all()
    for mydata in data:
        total_profit_month = total_profit_month + mydata.expense
    ctx = {"business": business, "total_profit_month": total_profit_month}
    return render(request, 'business/business_list.html',ctx)

def business_employees_view(request,id):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    employee = Employee.objects.all()
    return render(request, 'employee/employee_list.html',{'employee':employee})

def business_create_view(request):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
        
    context = {}
    if request.POST:
        form = BusinessForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context['form'] = form
    else:
        form = BusinessForm()
        context['form'] = form
    return render(request, 'business/business_create.html', context)

def business_edit_view(request,id):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    context = {}
    business = Business.objects.get(id=id)
    form = BusinessForm(request.POST or None, request.FILES or None, instance = business)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Not Valid')
    else:
        context['form'] = form
    return render(request, 'business/business_create.html', context)

def business_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('/employee/login')
    business = Business.objects.get(id=id)
    business.delete()
    return redirect("/")
