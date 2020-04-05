from django.contrib import admin

from . import models


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description','description_html']

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember



admin.site.register(models.Group,GroupAdmin)
