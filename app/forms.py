from django import forms
from app.models import *



class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['Address','Profile_pic']