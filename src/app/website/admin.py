import logging

from django.contrib import admin, messages

from .models import Item

logger = logging.getLogger("website.inventory")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "device_mac", "stock", "max_stock",
                    "row", "level", "box", "created_at")
    search_fields = ("name", "device_mac", "row", "level", "box")
    list_filter = ("row", "level", "box")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.needs_stock_warning():
            location = obj.location_label()
            logger.warning(
                "Stock warning: item_id=%s name=%s stock=%s max_stock=%s location=%s",
                obj.pk or "<unsaved>",
                obj.name,
                obj.stock,
                obj.max_stock,
                location,
            )
            self.message_user(
                request,
                f"Item '{obj.name}' at {location} has stock {obj.stock} exceeding the max of {obj.max_stock}.",
                level=messages.WARNING,
            )
