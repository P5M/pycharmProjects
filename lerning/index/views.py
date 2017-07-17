from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetail

# Create your views here.

def fillform(request):
    return render(request,'index.html',{})

def saveform(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    email=request.POST.get('email')
    # user_detail = UserDetail.objects.filter(name=name, password=password,email=email)
    # if user_detail.exists():
    #     return HttpResponse('already exist in database')
    user_detail=UserDetail.objects.create(name=name,password=password,email=email)
    return render(request,'valid.html')

# def validating(request):
#     return render(request,'valid.html',{})
#
# def check(request):
#     name1=request.POST.get('name')
#     password1=request.POST.get('password')
#     user_detail=UserDetail.objects.filter(name=name1,password=password1)
#     if user_detail.exists():
#         return HttpResponse('already exist')
#
#     return HttpResponse('no user exists')

