from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NameForm

def index(request):
    # return HttpResponse("Hello, World! This is a Django view.") # Here a using render module html and css pages can be returned to render 
    return render(request , 'index.html')
    # But the directory for the templates directory must be configured in the settings.py file  
def about(request):
    return HttpResponse("Hello, World! This is a Django website's about page")

def services(request):
    return HttpResponse("Hello, World! This is a Django website's services page")



def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Process the data
            print(f"Received name: {name}")
            return redirect('success')
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})



