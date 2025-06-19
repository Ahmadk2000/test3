from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # يمكنك تغييره حسب وجهة المستخدم بعد تسجيل الدخول
        else:
            context['not_found'] = True  # لتفعيل رسالة الخطأ في القالب

    return render(request, 'accounts/login.html', context)


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': 'كلمتا المرور غير متطابقتين'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'اسم المستخدم مستخدم بالفعل'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html')
