from django.views import View
from django.shortcuts import render

class CustomPageNotFoundPageView(View):
    def get(self, request, exception=None):
        return render(request, '404.html', status=404)