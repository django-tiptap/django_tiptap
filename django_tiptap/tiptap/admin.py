from django.contrib import admin

from django_tiptap.tiptap.models import Note

# Register your models here.
# admin.site.register(Note)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
