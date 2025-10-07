import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

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

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nama
    
class MataKuliah(models.Model):
    nama = models.CharField(max_length=255)
    mahasiswa = models.ManyToManyField(Mahasiswa)
    
    def __str__(self):
        return self.nama_mk
