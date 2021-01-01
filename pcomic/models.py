from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    tags = TaggableManager()
    main_image = models.FileField(blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    date_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
  
    def __str__(self):
        return self.title 
 
    def get_absolute_url(self):
        return reverse("pcomic:tags", kwargs={
            'slug': self.slug
        })

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.main_image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.main_image.path) 
  
  
class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField()

    def __str__(self):
        return self.post.title



