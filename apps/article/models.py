from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from apps.user.models import CustomUser
from django.utils.text import slugify
from apps.category.models import Category, Tag
from django.urls import reverse


class Article(BaseModel):
    name = models.CharField(max_length=300, unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, db_index=True)
    image_1 = models.ImageField(upload_to='aticle_images', default='images/default-image.jpg')
    image_2 = models.ImageField(upload_to='aticle_images', default='images/default-image.jpg')
    image_3 = models.ImageField(upload_to='aticle_images', default='images/default-image.jpg')
    description_1 = RichTextField(null=True, blank=True)
    description_2 = RichTextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    author = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='articles_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles_tags')
    views = models.IntegerField(default=0)
    for_banner = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('article-detail', kwargs={'slug': self.slug})
    

class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article')
    user = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True, related_name='comments_user')
    name = models.CharField(max_length=120, db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    web_site = models.URLField(max_length=100, db_index=True, unique=True, null=True, blank=True)
    comment = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'