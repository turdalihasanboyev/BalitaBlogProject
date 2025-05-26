from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import CustomUser
import re


def validate_email(email):
    # Email formatini tekshiradi
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validate_password(password):
    # Parol minimum 8 ta belgidan iborat bo‘lishini tekshiradi
    return len(password) >= 8


class RegisterPageView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
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
            
            # Emailni validatsiya qilish
            if not validate_email(email):
                messages.error(request, 'Email formati noto‘g‘ri!')
                return redirect('register')

            # Parol validatsiyasi
            if not validate_password(password):
                messages.error(request, 'Parol kamida 8 ta belgidan iborat bo‘lishi kerak!')
                return redirect('register')

            if password != confirm_password:
                messages.error(request, 'Parollar bir xil emas!')
                return redirect('register')

            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                description=description,
                image=image,
            )
            user.save()
            messages.success(request, "Foydalanuvchi muvaffaqiyatli ro'yhatdan o'tdi!")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Xatolik yuz berdi: {str(e)}")
            return redirect('register')


class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
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
        except Exception as e:
            messages.error(request, f"Xatolik yuz berdi: {str(e)}")
            return redirect('login')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        try:
            logout(request)
            messages.success(request, 'Tizimdan muvaffaqiyatli chiqdingiz!')
        except Exception as e:
            messages.error(request, f"Xatolik yuz berdi: {str(e)}")
        return redirect('home')