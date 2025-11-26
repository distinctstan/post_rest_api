from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Post

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','bio','profile_pic','facebook','youtube','instagram','twitter')

admin.site.register(CustomUser,CustomUserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','is_draft','category','created_at')

admin.site.register(Post,PostAdmin)