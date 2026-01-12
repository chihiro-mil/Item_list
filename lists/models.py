from django.db import models


class List(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    packing_list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="items",
    )
    name = models.CharField(max_length=30)
    memo = models.CharField(max_length=40, blank=True)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
