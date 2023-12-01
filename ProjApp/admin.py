from django.contrib import admin
from .models import SourceCategory, Source
# Register your models here.


@admin.register(Source)
class AdminSource(admin.ModelAdmin):
    list_display = ["id", "level", "username", "category",
                    "total_hits", "ratings", "channel_name"]


@admin.register(SourceCategory)
class AdminSourceCategory(admin.ModelAdmin):
    list_display = ["id", "name"]
