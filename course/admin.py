from django.contrib import admin
from .models import Destination, Company, UserProfile, Booking, Booking_status

# Register your models here.
admin.site.register(Destination)
admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Booking_status)

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission

from .models import UserProfile

# Register your models here.
admin.site.register(Permission)
admin.site.unregister(get_user_model())


class UserProfileInline(admin.StackedInline):
    """Create a Inline for UserProfile for Admin"""
    model = UserProfile
    fields = ('nationality', 'address', 'phone_number', 'wishlist')


class UserAdmin(BaseUserAdmin):
    inlines = [
        UserProfileInline,
    ]


# Now register the new UserAdmin...
admin.site.register(get_user_model(), UserAdmin)
