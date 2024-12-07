from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email allaqachon mavjud!')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Parollar bir xil emas!')
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            description=description,
            image=image,
            password=password,
            )
        user.save()
        messages.success(request, "Foydalanuvchi muvaffaqiyatli ro'yhatdan o'tdi!")
        return redirect('login')
    
    return render(request, 'register.html')

def login_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect('home')
        else:
            messages.error(request, 'Email yoki parol xato!')
            return redirect('login')
        
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Tizimdan muvaffaqiyatli chiqdingiz!')
    return redirect('home')