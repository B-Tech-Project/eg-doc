from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, ExtendedDoctorsDetail, ExtendedPatientsDetail


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password', 'name', 'is_doctor', 'is_patient', 'address',  'city', 'pin', 'state')}),
        ('Other details', {'fields': (
            'last_login',
            'is_active',
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'phone_number', 'password1', 'password2', 'name', 'is_doctor', 'is_patient', 'address', 'city', 'pin', 'state')
            }
        ),
    )

    list_display = ('email', 'phone_number', 'name', 'pin', 'is_doctor', 'is_patient')
    list_filter = ('is_superuser', 'is_active', 'is_doctor', 'is_patient')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin,)
admin.site.register(ExtendedDoctorsDetail)
admin.site.register(ExtendedPatientsDetail)
