from django.shortcuts import render, HttpResponse
from datetime import datetime
from Neo.models import Contact
from django.contrib import messages
# Create your views here.

context = {
        'varriable' : "this is sent",
        'var2' : 'lalalal'
}

def index(request):
    return render(request, 'index.html', context=context)
def about(request):
    # return HttpResponse("This is about page !")
    return render(request, 'about.html', context=context)
def services(request):
    # return HttpResponse("This is services page !")
    return render(request, 'services.html', context=context)
def contact(request):
    # return HttpResponse("This is contact page !")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, password=password, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !" )
    return render(request, 'contact.html', context=context)
def alpha(request):
    return render(request,'alpha.html', context=context)
def beta(request):
    return render(request,'beta.html', context=context)
def gamma(request):
    return render(request,'gamma.html', context=context)
