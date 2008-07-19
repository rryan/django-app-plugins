from django.contrib import admin
from app_plugins.models import PluginPoint, Plugin, UserPluginPreference

class PluginPointAdmin(admin.ModelAdmin):
    list_display = ('label', 'index', 'registered', 'status')
    list_filter = ('registered', 'status')

class PluginAdmin(admin.ModelAdmin):
    list_display = ('label', 'index', 'registered', 'required', 'status')
    list_filter = ('registered', 'status')

class UserPluginPreferenceAdmin(admin.ModelAdmin):
    list_display = ('plugin', 'user', 'index', 'visible')
    list_filter = ('visible',)

admin.site.register(PluginPoint, PluginPointAdmin)
admin.site.register(Plugin, PluginAdmin)
admin.site.register(UserPluginPreference, UserPluginPreferenceAdmin)

