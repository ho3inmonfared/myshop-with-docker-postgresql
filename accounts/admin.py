from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models,forms

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form=forms.CustomUserCreationForm
    form=forms.CustomUserChangeForm
    model=models.CustomUser
    list_display=['email','username','is_staff','is_active']
    list_filter=['is_staff','is_active']
    fieldsets=(
        (None,{'fields':('email','username','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','username','password1','password2','is_staff','is_active')
        }),
    )
    search_fields=['email','username']

