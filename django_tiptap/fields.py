from django.db import models
from django.forms import fields

from .widgets import TipTapWidget


class TipTapTextFormField(fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"widget": TipTapWidget()})
        super().__init__(*args, **kwargs)


class TipTapTextField(models.TextField):
    def formfield(self, **kwargs):
        return super().formfield(form_class=TipTapTextFormField, **kwargs)
