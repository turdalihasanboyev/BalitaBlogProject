from django.shortcuts import render
from django.views.generic import TemplateView
from apps.article.models import Article


class AboutPageView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_articles = Article.objects.filter(is_active=True).order_by('-created_at')[:10]
        context['last_articles'] = last_articles
        return context
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs))