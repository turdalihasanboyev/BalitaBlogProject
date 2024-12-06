from django.db import models
from apps.common.models import BaseModel
from django.utils.text import slugify
import uuid


class Category(BaseModel):
    name = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(max_length=225, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Tag(BaseModel):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"