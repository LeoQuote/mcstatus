from django.contrib import admin
from mc.models import Server
# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'directory', 'last_checked_at', 'last_started_at']


admin.site.register(Server, ServerAdmin)