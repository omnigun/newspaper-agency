from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Redactor, Topic, Newspaper


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


admin.site.register(Newspaper)
admin.site.register(Topic)

# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
# class NewspaperAdmin(admin.ModelAdmin):
    # search_fields = ("model",)
    # list_filter = ("manufacturer",)
