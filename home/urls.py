from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    # path('contact',views.contact_us,name='contact_us')
    path('contact',views.Contact_us.as_view(),name='contact_us')
]

