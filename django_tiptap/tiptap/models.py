from django.db import models
from tiptap.fields import TipTapTextField


# Create your models here.
class Note(models.Model):
    content = TipTapTextField()
    blueprint = TipTapTextField(null=True)
