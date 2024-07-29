from django.http import HttpResponse
# import render 

def index(request):
    return HttpResponse("Hello, World! This is a Django view.") # Here a using render module html and css pages can be returned to render 
    # return render(request , 'sample.html')
    # But the directory for the templates directory must be configured in the settings.py file  
def about(request):
    return HttpResponse("Hello, World! This is a Django website's about page")

def services(request):
    return HttpResponse("Hello, World! This is a Django website's services page")