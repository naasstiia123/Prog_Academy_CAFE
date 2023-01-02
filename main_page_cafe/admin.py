from django.contrib import admin
from .models import DishCategory, Dish, Description, Description_options, Reasons,  Events, Events_options, Galery, Book_table_F,\
    Contacts, Address, Email_adress, Phone_number, Testimonials, Chefs, Contacts_us, Hero

# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Description)
admin.site.register(Description_options)
admin.site.register(Reasons)
admin.site.register(Events)
admin.site.register(Events_options)
admin.site.register(Galery)
admin.site.register(Book_table_F)
admin.site.register(Chefs)
admin.site.register(Contacts)
admin.site.register(Address)
admin.site.register(Email_adress)
admin.site.register(Phone_number)
admin.site.register(Testimonials)
admin.site.register(Contacts_us)
admin.site.register(Hero)


