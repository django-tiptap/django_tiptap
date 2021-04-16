from django import forms


class TipTapWidget(forms.Textarea):
    class Media:
        js = (
            # "//cdn.skypack.dev/@tiptap/core?min",
            # "//cdn.skypack.dev/@tiptap/starter-kit?min",
            # "js/tiptap-min.js",
        )
        # html = ("html/index.html",)

    template_name = "forms/tiptap_textarea.html"

    def get_context(self, *args):
        context = super().get_context(*args)
        print(context)
        return context
