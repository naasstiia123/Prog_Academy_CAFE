from django.db import models
import os
import uuid
from django.utils import timezone
from django.core.validators import RegexValidator
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
    description1 = models.TextField(max_length=300, blank=True)
    is_visible = models.BooleanField(default=True)
    video = models.FileField(upload_to=get_file_name, blank=True)

class Description_options(models.Model):
    option = models.CharField(max_length=100)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.option}'

class Reasons(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    number = models.PositiveIntegerField(unique=True)
    description = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.position}'

class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.position}'

    class Meta:
        ordering = ('position', )

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
        return f'{self.name} {self.position}'

class Events_options(models.Model):

    option = models.CharField(max_length=100)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    event_category = models.ForeignKey(Events, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f'{self.option} {self.position}'

class Galery(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=100, blank=True)


class Chefs(models.Model, Import_file):
    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name)
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.position}'

class Testimonials(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    feedback = models.TextField(max_length=300)
    mark = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.position}'

class Contacts(models.Model):

    days_open = models.CharField(max_length=200)
    hours_open = models.TimeField(auto_now=False)
    hours_close = models.TimeField(auto_now=False)
    is_visible = models.BooleanField(default=True)
    map = models.URLField(max_length=200)

class Address(models.Model):

    address = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.address}'

class Email_adress(models.Model):

    email = models.EmailField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}'

class Phone_number(models.Model):

    phone_val = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='Не вірний формат номера')
    phone_num = models.CharField(max_length=16, validators=[phone_val])
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Contacts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.phone_num}'

class Contacts_us(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=300)

    date = models.DateField(auto_now=True)

    manager_date_processed = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email} {self.subject}'

class Book_table_F(models.Model):

    phone_val = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='Не вірний формат номера')


    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    phone_num = models.CharField(max_length=16, validators=[phone_val])
    persons = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=300, blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    manager_date_processed = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return f'{self.name} {self.phone_num}: {self.description[:20]}'


class Hero(models.Model, Import_file):

    def get_file_name(self, filename: str):
        return super().get_file_name(filename)

    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title} {self.position}'
