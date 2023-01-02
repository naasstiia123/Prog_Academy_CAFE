from django.shortcuts import render, redirect
import random
from .forms import Book_table_form, Contacts_us_form
from .models import DishCategory, Dish, Description, Description_options, Reasons,  \
    Events, Events_options, Galery,  Chefs, Testimonials, Contacts, Address, Phone_number, Email_adress, Hero


# Create your views here.
def view_main_page(request):
    if request.method == 'POST':
        form_reserve = Book_table_form(request.POST)
        form_contact = Contacts_us_form(request.POST)

        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

        if form_contact.is_valid():
            form_contact.save()
            return redirect('/')



    description = Description.objects.filter(is_visible=True)
    description_options = Description_options.objects.filter(is_visible=True)
    reasons = Reasons.objects.all()
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    events_option = Events_options.objects.filter(is_visible=True)
    gallery_photos = random.sample(list(Galery.objects.filter(is_visible=True)), 8)
    form_reserve = Book_table_form()
    chefs = Chefs.objects.filter(is_visible=True)
    feedback = Testimonials.objects.filter(is_visible=True)
    contacts = Contacts.objects.filter(is_visible=True)
    address = Address.objects.filter(is_visible=True)
    phone = Phone_number.objects.filter(is_visible=True)
    email = Email_adress.objects.filter(is_visible=True)
    form_contact = Contacts_us_form()
    hero = Hero.objects.filter(is_visible=True)
    hero = Hero.objects.filter(is_visible=True)


    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'description': description,
        'description_options': description_options,
        'reasons': reasons,
        'events': events,
        'events_option': events_option,
        'gallery_photos': gallery_photos,
        'form_reserve': form_reserve,
        'chefs': chefs,
        'feedback': feedback,
        'contacts': contacts,
        'address': address,
        'phone': phone,
        'email': email,
        'form_contact': form_contact,
        'hero': hero
    })


# def view_hero(request):
#     hero = Hero.objects.filter(is_visible=True)
#
#     return render(request, 'index.html', context={'hero': hero})
