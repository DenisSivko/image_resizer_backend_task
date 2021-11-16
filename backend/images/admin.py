from django.contrib import admin

from images.models import Images


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "url", "picture", "width", "height", "parent_picture"
    )
    list_filter = ("name",)
    search_fields = ("name",)
