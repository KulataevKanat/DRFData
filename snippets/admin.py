from django.contrib import admin

from snippets.models import Snippet, Users

admin.site.register(Snippet)
admin.site.register(Users)
