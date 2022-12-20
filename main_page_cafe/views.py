from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory, Dish, Description, Description_options, Reasons,  Events, Events_options

# Create your views here.
def view_main_page(request):
    description = Description.objects.filter(is_visible=True)
    description_options = Description_options.objects.filter(is_visible=True)
    reasons = Reasons.objects.all()
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    events_option = Events_options.objects.filter(is_visible=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'description': description,
        'description_options': description_options,
        'reasons': reasons,
        'events': events,
        'events_option': events_option
    })
