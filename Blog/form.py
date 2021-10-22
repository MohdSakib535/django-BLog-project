from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, UsernameField,AuthenticationForm,PasswordChangeForm
from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from django.http.request import MediaType
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post



class sign(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2=forms.CharField(label="confirm Password(again)",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    class Meta:
        model=User
        fields= ['username','first_name','last_name','email'] 
        labels={'email':'Email'}
        
        
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'first_name':forms.TextInput(attrs={'class':"form-control"}),
            'last_name':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.TextInput(attrs={'class':"form-control"}),

        }

class Login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':"form-control"}),error_messages={'required':'Username is compulsory'})
    password=forms.CharField(
        label=_("password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':"form-control"}),
        error_messages={'required':"Password is compulsory"},
    )
  
        
class Edit_Pofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']
        widgets={
            "username":forms.TextInput(attrs={'class':"form-control"}),
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "last_name":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "last_login":forms.DateTimeInput(attrs={'class':"form-control"}),
            "date_joined":forms.DateTimeInput(attrs={'class':"form-control"}),
            "is_active":forms.CheckboxInput(attrs={'class':'class1'}),

        }
        # fields="_


class EditPassword(PasswordChangeForm):
    old_password=forms.CharField(label="Old Password",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    new_password1=forms.CharField(label="New Password",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    new_password2=forms.CharField(label="New Password(Confirm)",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    class Meta:
        model:User

       





class Admin_Pofile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active','is_superuser']
        widgets={
            "username":forms.TextInput(attrs={'class':"form-control"}),
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "last_name":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "last_login":forms.DateTimeInput(attrs={'class':"form-control"}),
            "date_joined":forms.DateTimeInput(attrs={'class':"form-control"}),
            "is_active":forms.CheckboxInput(attrs={'class':'class1'}),
            "is_superuser":forms.CheckboxInput(attrs={'class':'class1'}),

        }

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=["Title","Desc"]
        widgets={
            "Title":forms.TextInput(attrs={'class':"form-control"}),
            "Desc":forms.Textarea(attrs={'class':"form-control"}),
        }


