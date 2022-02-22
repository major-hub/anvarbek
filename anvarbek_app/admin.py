from django.contrib import admin

from .models import Categories, Products


@admin.register(Categories)
class adminCategories(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    ordering = ("pk",)


@admin.register(Products)
class adminProducts(admin.ModelAdmin):
    list_display = ("pk", "title", "time_create", "category", "is_published")
    list_editable = ("is_published",)
    list_display_links = ("pk",)
    search_fields = ("title", "desc")
    list_filter = ("time_create", "time_update")

    ordering = ("pk", )
