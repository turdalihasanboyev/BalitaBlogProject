from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField


class Contact(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, db_index=True, null=True, blank=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Biz bilan aloqa"
        verbose_name_plural = "Biz bilan aloqa"