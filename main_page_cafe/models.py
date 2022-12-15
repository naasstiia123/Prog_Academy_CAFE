from django.db import models
import os
import uuid
# Create your models here.

class Import_file:

   def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('file/dishes', filename)


class Description(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    description = models.TextField(max_length=300)
    is_visible = models.BooleanField(default=True)
    video = models.FileField(upload_to=get_file_name)


class Description_options(models.Model):
    option = models.CharField(max_length=100)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)


class Reasons(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    number = models.PositiveIntegerField(unique=True)
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        f'{self.name} {self.position}'

class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}{self.position}'



class Dish(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)


    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name} {self.position}'


class SpecialDish(models.Model):
    name = models.ForeignKey(Dish, related_name='dish_name', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)
    description = models.TextField(max_length=200, blank=True)
    ingredients = models.ForeignKey(Dish, related_name='dish_ingredients', on_delete=models.CASCADE)
    photo = models.ForeignKey(Dish, related_name='dish_photo', on_delete=models.CASCADE)

    def __str__(self):
        f'{self.name} {self.position}'


class Events(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        f'{self.name} {self.position}'

class Events_options(models.Model):

    option = models.CharField(max_length=100)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    event_category = models.ForeignKey(Events, on_delete=models.CASCADE)


