import uuid
from django.db import models
import datetime as dt

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    
    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_upload = models.ImageField(blank=True, manual_crop="800x800")
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, null=True)
    image_category = models.ForeignKey(Category, null=True)
    image_time_created = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.image_description

    class Meta:
        ordering=['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image_link=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def get_image_by_name(cls, name):
        images = cls.objects.filter(image_name__icontains=name).all()
        return images

    @classmethod
    def get_image_by_location(cls, location):
        images = Image.objects.filter(image_location__location_name=location)
        return images

    @classmethod
    def get_image_by_category(cls, category):
        images = cls.objects.filter(image_category__category_name__icontains=category).all()
        return images

    
class Location(models.Model):
    location_name = models.CharField(max_length=150)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    
    @classmethod
    def update_location(cls, id, new_location):
        cls.objects.filter(id=id).update(location_name=new_location)

class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
    @classmethod
    def update_category(cls, id, new_category):
        cls.objects.filter(id=id).update(category_name=new_category)
