from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .forms import UserCreationForm, UserChangeForm

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username', 'about', 'is_staff', ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'about'),
        }),
    )


admin.site.register(User, UserAdmin)
