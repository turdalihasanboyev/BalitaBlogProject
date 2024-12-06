from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from apps.article.models import Article, Comment


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        banner = Article.objects.filter(for_banner=True, is_active=True).order_by('id')
        last_articles = Article.objects.filter(is_active=True).order_by('-id')[:3]
        articles = Article.objects.filter(is_active=True).order_by('-created_at')[:8]
        more_articles = Article.objects.filter(is_active=True).order_by('-created_at')[:3]

        context = {
            'banner':  banner,
            'last_articles': last_articles,
            'articles': articles,
            'more_articles': more_articles,
        }

        return render(request, self.template_name, context)
    

class ArticleDetailView(View):
    template_name = 'blog-single.html'

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug, is_active=True)
        comments = Comment.objects.filter(is_active=True, article=article).order_by('-id')
        related_articles = Article.objects.filter(is_active=True, category=article.category).order_by('-id')[:3]

        context = {
            'article': article,
            'comments': comments,
            'related_articles': related_articles,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug__iexact=slug, is_active=True)

        comment = Comment()
        comment.user = request.user
        comment.article = article
        comment.name = request.POST.get('name')
        comment.email = request.POST.get('email')
        comment.web_site = request.POST.get('web_site')
        comment.comment = request.POST.get("comment")

        comment.save()

        return redirect('article-detail', slug__exact=slug)