from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
import os

# Hàm đổi tên file ảnh
def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{slugify(instance.title)}.{ext}"
    return os.path.join('images/', filename)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    contact = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,null=True, blank=True)
    article = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Tự động lấy thời gian tạo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=500, verbose_name="Website Link")
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Tự động lấy thời gian tạo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
