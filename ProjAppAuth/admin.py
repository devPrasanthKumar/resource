from django.contrib import admin

from ProjAppAuth.models import CustomPermission, User

# Register your models here.


@admin.register(User)
class AdminSourceCategory(admin.ModelAdmin):
    list_display = ["id", "username", "email", "userMode"]


@admin.register(CustomPermission)
class AdminPermission(admin.ModelAdmin):
    list_display = ["id", "userName", "can_edit", "can_delete"]
