from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    #text = """<h1>welcome to my app !</h1>"""
    return render(request,'hello.html',{})
def abc(request):
    #text = """<h1>welcome to my app !</h1>"""
    return render(request,'SSC.html',{})