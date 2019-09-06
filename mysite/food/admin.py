from django.contrib import admin
from .models import UserData
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    fields = ('user_location', 'user_search_radius', 'user_star_standard')

admin.site.register(UserData, LocationAdmin)
