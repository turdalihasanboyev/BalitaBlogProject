from apps.category.models import Category, Tag
from apps.article.models import Article

def global_context_object(request):
    categories = Category.objects.filter(is_active=True).order_by('name')
    tags = Tag.objects.filter(is_active=True).order_by('name')
    popular_articles = Article.objects.filter(is_active=True).order_by('-views')[:3]
    latest_articles = Article.objects.filter(is_active=True).order_by('-created_at')[:3]

    context = {}

    context['categories'] = categories
    context['tags'] = tags
    context['popular_articles'] = popular_articles
    context['latest_articles'] = latest_articles

    return context