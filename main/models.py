import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('footwear', 'Footwear'),
        ('jersey', 'Jersey'),
        ('shin guard', 'Shin Guard'),
        ('gloves', 'Gloves'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()
