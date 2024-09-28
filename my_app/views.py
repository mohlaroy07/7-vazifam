from django.shortcuts import render
from .models import Category, Phone

def home(request):
    category = Category.objects.all()
    phone = Phone.objects.all()
    
    context = {
        "categories": category,
        "phones": phone         
    }
    
    return render(request, "index.html", context)