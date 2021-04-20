from django import forms


class TipTapWidget(forms.Textarea):
    class Media:
        css = {"all": ("css/styles-min.css",)}

    template_name = "forms/tiptap_textarea.html"
