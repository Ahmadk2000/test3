from django.shortcuts import render
from .models import Product

def home_view(request):
    # جلب المنتجات المتوفرة وترتيبها من الأحدث إلى الأقدم
    products = Product.objects.filter(available=True).order_by('-created_at')
    return render(request, 'home.html', {'products': products})
