from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import User



def loginPage(request):
    if request.method == 'POST':
        name=request.POST.get('Name')
        FatherName=request.POST.get('FatherName')
        Address=request.POST.get('Address')
        MobileNo=request.POST.get('MobileNo')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        add= User.objects.create(name=name,fathername=FatherName,address=Address,mobileno=MobileNo,email=Email,password=Password)
        return redirect('view')
    return render(request,'login.html',{})


def view(request):
    context={}
    if request.method =='GET':

        result = User.objects.all()
        context = {
            'results': result
        }
    return render(request, 'list.html', context)


def editPage(request,id=None):
    user_object= {}
    if request.method == 'POST':
        name=request.POST.get('name')
        FatherName=request.POST.get('fathername')
        Address=request.POST.get('address')
        MobileNo=request.POST.get('mobileno')
        Email=request.POST.get('email')
        password=request.POST.get('password')
        if id:
            front_end_obj = User.objects.get(id=id)
            front_end_obj.name = name
            front_end_obj.fathername = FatherName
            front_end_obj.address = Address
            front_end_obj.mobileno = MobileNo
            front_end_obj.email = Email
            front_end_obj.password = password
            front_end_obj.save()

        return redirect('view')
    if id is not None:
       user_object =  User.objects.get(id=id)
    return render(request,'editPage.html',{'user_object':user_object})




def deleteRecord(request,id=None):
    object_delete = User.objects.get(id=id)
    object_delete.delete()
    return redirect('view')