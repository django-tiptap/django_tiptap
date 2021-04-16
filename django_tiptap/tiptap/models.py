from django.db import models

from django_tiptap.tiptap.fields import TipTapTextField


# Create your models here.
class Note(models.Model):
    content = TipTapTextField()
