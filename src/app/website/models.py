from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    device_mac = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    max_stock = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    row = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])
    box = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    def __str__(self):
        return (f"{self.name} {self.stock} {self.max_stock} {self.row} {self.level} {self.box} {self.created_at} {self.device_mac}")

    def clean(self):
        super().clean()

    def location_label(self) -> str:
        return f"R{self.row}-E{self.level}-K{self.box}"

    def needs_stock_warning(self) -> bool:
        return (
            self.stock is not None
            and self.max_stock is not None
            and self.stock >= self.max_stock
        )
