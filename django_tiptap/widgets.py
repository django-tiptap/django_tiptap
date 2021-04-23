from typing import Any, Dict

from django import forms
from django.conf import settings

from .config import TIPTAP_DEFAULT_CONFIG, TIPTAP_DEFAULT_TOOLTIPS


class TipTapWidget(forms.Textarea):
    class Media:
        css = {"all": ("css/styles-min.css",)}

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

        if (context["widget"]["config"].get("tooltips")):
            return context
        elif (context["widget"]["config"].get("lang")):
            langs: list = ["EN", "DE"]
            givenLang: str = context["widget"]["config"].get("lang")

            if (givenLang.upper() in langs):
                context["widget"]["config"]["tooltips"] = TIPTAP_DEFAULT_TOOLTIPS.copy()[givenLang.upper()]
            else:
                context["widget"]["config"]["tooltips"] = TIPTAP_DEFAULT_TOOLTIPS.copy()["EN"]
                print('\n *** The language given to django_tiptap was not found, using english as default. *** \n')
        else: 
            context["widget"]["config"]["tooltips"] = TIPTAP_DEFAULT_TOOLTIPS.copy()["EN"]

        return context
