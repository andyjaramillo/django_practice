from django.contrib import admin
from . import models
# Register your models here.
#modifies the django admin interface
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
#adds the notes to the admin page
admin.site.register(models.Notes, NotesAdmin) 