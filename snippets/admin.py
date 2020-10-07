from django.contrib import admin

from snippets.models import Snippet, User

admin.site.register(Snippet)
admin.site.register(User)
