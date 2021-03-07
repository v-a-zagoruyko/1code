from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *

admin.site.site_header = '1CODE'
admin.site.site_title = 'Панель администрирования'
admin.site.index_title = 'Главная'

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    fieldsets = (
        ('Регистрационные данные', {'fields': ('email', 'first_name', 'last_name', 'is_active')}),
    )

    list_display = ('full_name', 'email', 'phone',)
    search_fields = ('first_name', 'last_name', 'email',)

    def phone(self, obj):
      return obj.profile.phone

    def has_delete_permission(self, request, obj=None):
        return False