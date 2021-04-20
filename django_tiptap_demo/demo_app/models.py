from django.db import models

from django_tiptap.fields import TipTapTextField


# Create your models here.
class Note(models.Model):
    content = TipTapTextField()
    somethingMore = TipTapTextField(null=True)
