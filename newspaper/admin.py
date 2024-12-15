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


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]



@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "topic__name", "published_date"]
    list_display_links = ["title"]
    ordering = ("published_date", "pk")