from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html', context=context)
