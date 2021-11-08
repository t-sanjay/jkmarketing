from django.contrib import admin

from tutorials.models import Users

# Register your models here.
@admin.register(Users)
class UsersData(admin.ModelAdmin):
      list_display = ("id","zip_code", "first_name", "primary_phone")