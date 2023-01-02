from django.shortcuts import render, redirect
from main_page_cafe.models import Book_table_F, Contacts_us, Hero
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def is_manager(user):
    return user.groups.filter(name='managers').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations(request):
    messages = Book_table_F.objects.filter(is_processed=False)
    hero = Hero.objects.filter(is_visible=True)
    return render(request, 'reservation.html', context={'reservations': messages, 'hero': hero})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update(request, pk):
    Book_table_F.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def feedback(request):
    massages = Contacts_us.objects.filter(is_processed=False)
    hero = Hero.objects.filter(is_visible=True)
    return render(request, 'feedback.html', context={'feedback': massages, 'hero': hero})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def up_feedback(request, pk):
    Contacts_us.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:feedback')

