from django.shortcuts import render

from django.views import View


class CustomPageNotFoundPageView(View):
    template_name = '404.html'

    def get(self, request, exception=None):
        return render(request, self.template_name, status=404)
