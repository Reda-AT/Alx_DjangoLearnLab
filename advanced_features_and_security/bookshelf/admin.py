from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be displayed in the 'add user' form in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'phone_number', 'profile_photo'),
        }),
    )

    # Specify the fields to be displayed in the user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'phone_number')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

# Register the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
