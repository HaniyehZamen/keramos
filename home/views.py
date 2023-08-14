from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})

# def contact_us(request):
#     return render(request,'contact_us.html',{})

class Contact_us (TemplateView):
    template_name = 'contact_us.html'