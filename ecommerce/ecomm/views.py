from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

def home(request):
    item = product.objects.all()
    return render(request,'home.html',{'item': item})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if person.objects.filter(email = email).exists():
            messages.error(request,'email is already exists')
            return redirect('/contact/')
        else:
            person.objects.create(name=name,email=email,subject=subject,message=message)
            messages.success(request,'Details Add Successfully ')
            details = person.objects.all()
            return render(request,'contact.html',{'details': details })


     
    # return render(request,'contact_us.html')

# Create your views here.
