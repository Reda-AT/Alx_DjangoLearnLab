from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
# Register your models here.
admin.site.register(Book, BookAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
