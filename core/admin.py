from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Catalogue, Formation, Section, Users

# Register your models here.
admin.site.register(Catalogue)
admin.site.register(Formation)
admin.site.register(Section)
admin.site.register(Users)


class UserAdminConfig(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': (
        'email', 'password', 'first_name', 'last_name')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',
                       'is_active', 'is_staff')}
         ),
    )
