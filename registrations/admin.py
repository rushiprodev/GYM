from django.contrib import admin
from .models import YogaRegistration, OnlineRegistration, OfflineRegistration

@admin.register(YogaRegistration)
class YogaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'submission_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('branch', 'health_condition')

@admin.register(OfflineRegistration)
class OfflineAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'year_of_study')
    search_fields = ('first_name', 'last_name', 'email', 'roll_no')
    list_filter = ('year_of_study', 'gender')

@admin.register(OnlineRegistration)
class OnlineAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'year_of_study')
    search_fields = ('first_name', 'last_name', 'email', 'roll_no')
    list_filter = ('year_of_study', 'gender')
