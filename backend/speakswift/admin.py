from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "level",
    )
    list_filter = (
        "email",
    )


admin.site.register(User, UserAdmin)
