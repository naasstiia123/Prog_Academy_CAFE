from django.contrib import admin
from .models import DishCategory, Dish, Description, Description_options, Reasons,  Events, Events_options

# Register your models here.
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Description)
admin.site.register(Description_options)
admin.site.register(Reasons)
admin.site.register(Events)
admin.site.register(Events_options)