from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from api.models import UserKey, Image, UserRelation

class UserKeyInline(admin.StackedInline):
    model = UserKey
    can_delete = False
    verbose_name_plural = 'user keys'

class UserAdmin(BaseUserAdmin):
    inlines = (UserKeyInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Image)
admin.site.register(UserRelation)
