from django.contrib import admin
from .models import Region, District, Job, Application

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    list_filter = ['region']
    search_fields = ['name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'region', 'district', 'status', 'end_date']
    list_filter = ['status', 'region', 'job_type', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at', 'is_expired']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'worker', 'job', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['worker__username', 'job__title']

