from django.contrib import admin
from .models import List, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    ordering = ("-updated_at",)
    search_fields = ("title",)
    inlines = [ItemInline]
