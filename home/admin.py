from django.contrib import admin

from . import models


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('book_name',)}

admin.site.register(models.Book, BookAdmin)

