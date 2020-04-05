from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','message','message_html','group']

admin.site.register(models.Post,PostAdmin)
