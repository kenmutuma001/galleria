
from django.db import models
import datetime as dt

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=70)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default="general")
    image_url = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        # if len(images) < 1:
        #     case_images = cls.objects.filter(
        #         Category__name__contains=search_term.capitalize())
        #     return case_images
        # else:
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def filter_by_location(cls, search_term):
        location = Location.objects.get(name=search_term)
        images = cls.objects.filter(location=location)
        return images
