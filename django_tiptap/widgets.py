from typing import Any, Dict

from django import forms
from django.conf import settings

from .config import TIPTAP_DEFAULT_CONFIG, getUpdatedContextForProperty


class TipTapWidget(forms.Textarea):
    class Media:
        css = {"all": ("django_tiptap/css/styles-min.css",)}

    template_name = "forms/tiptap_textarea.html"

    def __init__(self, config: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = self.set_config(config)

    @staticmethod
    def set_config(config: dict = None) -> dict:
        # Take default config and update it with the user config from settings.py.

        config = config.copy() if config else TIPTAP_DEFAULT_CONFIG.copy()
        django_settings_config = getattr(settings, "DJANGO_TIPTAP_CONFIG", {})
        config.update(django_settings_config)

        return config

    def get_context(self, *args, **kwargs) -> Dict[str, Any]:
        context = super().get_context(*args, **kwargs)
        context["widget"]["config"] = self.config

        context = getUpdatedContextForProperty(context, "tooltips")

        context = getUpdatedContextForProperty(context, "translations")

        return context
