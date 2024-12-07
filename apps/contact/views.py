from django.shortcuts import render, redirect
from django.views import View
from .models import Contact


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
        contact.save()
        return redirect(url)