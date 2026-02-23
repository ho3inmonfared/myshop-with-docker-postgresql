from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=('email','username',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=models.CustomUser
        fields=('email','username',)