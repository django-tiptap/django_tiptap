# django_tiptap

Django admin TipTap integration. Provides a `TipTapTextField` and `TipTapWidget` that
allow you to use TipTap in your Django forms and admin pages.

For more information about TipTap, check out [tiptap.dev](https://www.tiptap.dev/).

https://user-images.githubusercontent.com/45892659/115373320-0d17dc80-a1cc-11eb-89da-c5f723a19c63.mov

# Installation

1. Install or add django_tiptap to your PythonPath:

   ```bash
   pip install django_tiptap
   ```

2. Add django_tiptap to your `INSTALLED_APPS` in Djangos `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ...
       "django_tiptap",
   ]
   ```

# Usage

## Field

To add HTML WYSIWYG text editing capabilities to your models use the `TipTapTextField`
model field. It is a subclass of Djangos `TextField` configured to use the
`TipTapWidget` by default.
<br>

```python
from django.db import models

from django_tiptap.fields import TipTapTextField


class Note(models.Model):
    content = TipTapTextField()
```

## Widget

You can also use the `TipTapWidget` directly when defining a custom form.
<br>

```python

from django import forms
from django.contrib import admin
from django_tiptap.widgets import TipTapWidget

from demo_app.models import Note

class NoteAdminForm(forms.ModelForm):
    content = forms.TextField(widget=TipTapWidget())

    class Meta:
        model = Note
        fields = '__all__'

class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm

admin.site.register(Note, NoteAdminForm)
```

## Configuration

You can configure some of the editor behaviour by modifying the `DJANGO_TIPTAP_CONFIG` dict in `settings.py`.

```python
DJANGO_TIPTAP_CONFIG = {
    "width": "500px",
    "height": "500px",
    "extensions": [
        # to see what each extension does, refer to [tiptap.dev](https://www.tiptap.dev/)
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "textAlign",
        "indent",
        "table",
        "bulletList",
        "orderedList",
        "typography",
        "clearFormat"
    ],
    "placeholderText": "Begin typing here...",  # set None to skip display
    "unsavedChangesWarningText": "You have unsaved changes",  # set None to skip display
    "lang": "EN" # if you want to use default tooltips and translations, use this. Valid Options => EN/DE(for now)
    "tooltips": {
        # if you want to use your custom tooltips(maybe because you don't prefer default or the language you want isn't there)
        "bold": "Bold | (ctrl / ⌘) + B",
        "italic": "Italic | (ctrl / ⌘) + I",
        "underline": "Underline | (ctrl / ⌘) + U",
        "strike": "Strikethrough | (ctrl / ⌘) + shift + X",
        "h1": "Header 1 | (ctrl + alt) / (⌘ + ⌥) + 1",
        "h2": "Header 2 | (ctrl + alt) / (⌘ + ⌥) + 2",
        "h3": "Header 3 | (ctrl + alt) / (⌘ + ⌥) + 3",
        "h4": "Header 4 | (ctrl + alt) / (⌘ + ⌥) + 4",
        "h5": "Header 5 | (ctrl + alt) / (⌘ + ⌥) + 5",
        "h6": "Header 6 | (ctrl + alt) / (⌘ + ⌥) + 6",
        "alignLeft": "Align Left | (ctrl + shift ⇧) / (⌘ + shift ⇧) + L",
        "alignCenter": "Align Center | (ctrl + shift ⇧) / (⌘ + shift ⇧) + E",
        "alignRight": "Align Right | (ctrl + shift ⇧) / (⌘ + shift ⇧) + R",
        "alignJustify": "Justify | (ctrl + shift ⇧) / (⌘ + shift ⇧) + J",
        "indent": "Indent (Tab ↹)",
        "outdent": "Outdent (shift ⇧ + Tab ↹)",
        "bulletList": "Bullet List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 8",
        "orderedList": "Numbered List | (ctrl + shift ⇧) / (⌘ + shift ⇧) + 7",
        "addTable": "Add Table",
        "deleteTable": "Delete Table",
        "addColumnBefore": "Add Column Before",
        "addColumnAfter": "Add Column After",
        "deleteColumn": "Delete Column",
        "addRowBefore": "Add Row Before",
        "addRowAfter": "Add Row After",
        "deleteRow": "Delete Row",
        "mergeCells": "Merge Cells",
        "splitCell": "Split Cell",
        "toggleHeaderColumn": "Toggle Header Column",
        "toggleHeaderRow": "Toggle Header Row",
        "toggleHeaderCell": "Toggle Header Cell",
        "clearFormat": "Clear Format",
    },
    "translations": {
        # if the lang you defined exists in the default langs, then no need to define translations
        "row": "Row",
        "column": "Column",
        "add": "Add"
    },
    "custom_extensions": []

}
```

### Custom extensions

You can specify custom tiptap extensions that should be loaded using the `custom_extensions` config list.
This list contains dictionaries with the following options:

* `source_static` or `source_url`: where to load the extension from (**mandatory**)
* `module_name` the name of the extension (**mandatory**)
* `configuration_statement` how to configure the extension. Defaults to the `module_name` if not set
* `toolbar_include` path of a html-template to include into the toolbar
* `buttonsconfig_include` path of a js-template to include into the tiptap buttonsconfig
* `css_include` path of a css-template to include into the textarea

`django_tiptap_demo` contains an example of a custom extension

# Contributing

This project is a very rough draft of what a TipTap Editor experience in Django could
look like. If you're missing a feature and want to contribute to this project you are more than
welcome to!

## Development

1.  We use black and isort to auto-format the code base. Both are set up as pre-commit hooks and in the tox testmatrix.

    ```bash
    pip install black isort pre-commit
    pre-commit install
    ```

2.  For development purposes it is encouraged to add the `django_tiptap` and
    `django_tiptap_demo` modules to your PythonPath. You can either configure this via
    your shell of choice or through your IDE.
    VSCode users can use the following setting to automatically add the current workspace
    to the PythonPath. If you're an OSX/MacOS user, replace `env.linux` with `env.osx`.

    ```json
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}"
    },
    ```
