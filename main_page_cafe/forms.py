from django import forms
from .models import Book_table_F, Contacts_us

class Book_table_form(forms.ModelForm):
    class Meta:
        model = Book_table_F
        fields = ('name',
                  'mail',
                  'phone_num',
                  'persons',
                  'description')

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                                'type':"text",
                                                                'name':"name",
                                                                'class':"form-control",
                                                                'id':"name",
                                                                'placeholder':"Your Name",
                                                                'data-rule':"minlen:4",
                                                                'data-msg':"Please enter at least 4 chars"}))
    mail = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
                                                                'type':"email",
                                                                'class':"form-control",
                                                                'name':"email", 'id':"email",
                                                                'placeholder':"Your Email",
                                                                'data-rule':"email",
                                                                'data-msg':"Please enter a valid email"}))
    phone_num = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
                                                                'type':"text",
                                                                'class':"form-control",
                                                                'name':"phone",
                                                                'id':"phone",
                                                                'placeholder':"Your Phone",
                                                                'data-rule':"minlen:4",
                                                                'data-msg':"Please enter at least 4 chars"}))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                                                                'type':"number",
                                                                'class':"form-control",
                                                                'name':"people",
                                                                'id':"people",
                                                                'placeholder':"# of people",
                                                                'data-rule':"minlen:1",
                                                                'data-msg':"Please enter at least 1 chars"}))
    description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
                                                                'class':"form-control",
                                                                'name':"message",
                                                                'rows':"5",
                                                                'placeholder':"Message"}))


class Contacts_us_form(forms.ModelForm):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                                        'type':"text",
                                                                        'name':"name",
                                                                        'class':"form-control",
                                                                        'id':"name",
                                                                        'placeholder':"Your Name"
                                                                    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                                                        'type':"email",
                                                                        'class':"form-control",
                                                                        'name':"email",
                                                                        'id':"email",
                                                                        'placeholder':"Your Email"
                                                                    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
                                                                        'type':"text",
                                                                        'class':"form-control",
                                                                        'name':"subject",
                                                                        'id':"subject",
                                                                        'placeholder':"Subject"
                                                                        }))
    message = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
                                                                        'class':"form-control",
                                                                        'name':"message",
                                                                        'rows':"5",
                                                                        'placeholder':"Message"}))


    class Meta:

        model = Contacts_us
        fields = ('name',
                  'email',
                  'subject',
                  'message')
