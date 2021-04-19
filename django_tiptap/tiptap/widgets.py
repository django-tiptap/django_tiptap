from django import forms


class TipTapWidget(forms.Textarea):
    class Media:
        css = {"all": ("css/styles.min-min.css",)}

    template_name = "forms/tiptap_textarea.html"

    def get_context(self, *args):
        context = super().get_context(*args)
        print(context)
        return context
