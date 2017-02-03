from django import forms
from django_summernote.admin import SummernoteWidget
from .models import Genre

genre=[]
genre_elem = Genre.objects.all()
count = len(genre_elem)
for i in range(0,count):
    genre.append((str(genre_elem[i]),str(genre_elem[i])))


class UserRegister(forms.Form):
    user_name = forms.CharField(required="true", label="user name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    first_name = forms.CharField(required="true", label="first name", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required="true", label="last name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required="true", label="email id", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address",
                              widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    contact = forms.IntegerField(required="true", widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
    widgets = {
        'password': forms.PasswordInput(),
    }


class CompanyRegister(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20,
                                   widget=forms.TextInput(attrs={'placeholder': 'Company Name'})
                                   )
    first_name = forms.CharField(required="true", label="first name", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required="true", label="last name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required="true", label="email id",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address",
                              widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    contact = forms.IntegerField(required="true", widget=forms.TextInput(attrs={'placeholder': 'Contact'}))
    widgets = {
        'password': forms.PasswordInput(),

    }


class JobSubmit(forms.Form):
    genre = forms.ChoiceField(choices=genre,required="true")
    details = forms.CharField(required="true", label="Job Details", max_length=200000,
                              widget=SummernoteWidget(
                                  attrs={'placeholder': 'Details', 'width': '100%', 'height': '300px'}))
    pay = forms.IntegerField(required="true", widget=forms.TextInput(attrs={'placeholder': 'Pay(In Thousand)'}))
    dead_line = forms.IntegerField(required="true", label="Dead Line(In Days)",
                                widget=forms.TextInput(attrs={'placeholder': 'Deadline'}))


class ApplicationSubmit(forms.Form):
    application = forms.CharField(required="true", widget=SummernoteWidget(
        attrs={'placeholder': 'Details', 'width': '90%', 'height': '500px'}), label="Job Application",
                                  max_length=200000)
    pay_expected = forms.IntegerField(required="true")


class ProfileAdd(forms.Form):
    profile_img = forms.ImageField(required=False)
    website_linked = forms.URLField(required=False, label="Link your Website")
    user_introduction = forms.CharField(widget=SummernoteWidget(
                                  attrs={'placeholder': 'Details', 'width': '90%', 'height': '300px'}),required=False, label="Self Introduction")


class LogInUser(forms.Form):
    user_name = forms.CharField(required="true", label="User name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class LogInCompany(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20,
                                   widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class SearchJob(forms.Form):
    search = forms.ChoiceField(choices=genre,required="true",label='Genre')
    pay_Salary = forms.IntegerField(required="true")
