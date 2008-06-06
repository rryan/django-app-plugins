from django.conf import settings
from django import template
from django.template import loader
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.core.cache.backends.locmem import CacheClass as LocalMemCache
import re

APP_PLUGINS_CACHE_PARAMS = getattr(settings, 'APP_PLUGINS_CACHE_PARAMS',
                                     {'cull_frequency': 4,
                                      'max_entries': 3000,
                                     'timeout': 60*60*24*3, # 3 days
                                     })

app_plugin_apps_with_templates = LocalMemCache('localhost', APP_PLUGINS_CACHE_PARAMS)

NAME_RE = re.compile('^[a-zA-Z0-9_.]+$')

# at import cache the app names for indexing
app_names = []
for app in settings.INSTALLED_APPS:
    name = app.split('.')[-1]
    if name not in app_names:
        app_names.append(name)
app_names = tuple(app_names)

register = template.Library()

@register.filter
def template_exists(templ):
    if templ is None: return False
    try:
        #loader.get_template(templ)
        loader.find_template_source(templ)
    except TemplateDoesNotExist:
        return False
    return True

def validate_name(name):
    ## red_flag: turn into a string
    if not NAME_RE.match(name):
        raise TemplateSyntaxError, "invalid plugin point name."

def construct_template_path(app, name, ext='.html'):
    validate_name(name)
    validate_name(app)
    return '/'.join([app.split('.')[-1], 'plugins', name.replace('.','/')]) + ext

@register.inclusion_tag("app_plugins/app_plugin.html", takes_context=True)
def app_plugin(context, app, name, ext='.html'):
    nc = context
    nc['app_plugin_app'] = app
    nc['app_plugin_point'] = name
    nc['app_plugin_template'] = construct_template_path(app, name, ext)
    return nc

@register.inclusion_tag("app_plugins/plugin_point.html", takes_context=True)
def plugin_point(context, name, ext='.html'):
    validate_name(name)
    nc = context
    nc['app_plugin_ext'] = ext
    nc['app_plugin_point'] = name
    apps = app_plugin_apps_with_templates.get(name, None)
    if apps is None:
        tpls = ((app, construct_template_path(app, name, ext)) for app in app_names)
        apps = [ app for app, tpl in tpls if template_exists(tpl) ]
        app_plugin_apps_with_templates.set(name, apps)
    nc['app_plugin_apps'] = apps
    return nc
