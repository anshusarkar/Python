
from django.contrib import admin
from django.urls import path
from Neo import views

# To make changes in the admin text in the admin panel uncommen the below text and make chnages in the strings

# admin.site.site_header = "XYZ"
# admin.site.site_title = "XYZ admin portal"
# admin.site.index_title = "Welcome to the XYZ research portal"

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contact, name = 'contact'),
    path('admin/', admin.site.urls),
    path('alpha/', views.alpha, name= 'alpha'),
    path('beta/', views.beta, name='beta'),
    path('gamma/', views.gamma, name='gamma')
]
