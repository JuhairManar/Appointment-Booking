from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


# admin.site.register(UserProfile)

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display=['creator','title','category','truncated_summary', 'truncated_content','save_as_draft']
    
    
    def creator(self,obj):
        return obj.userprofile.username
    
    def truncated_summary(self,obj):
        words = obj.summary.split()
        if len(words) > 5: 
            truncated_summary = ' '.join(words[:5]) + '...'  
        else:
            truncated_summary = ' '.join(words) 
            
        return truncated_summary
    
    def truncated_content(self,obj):
        words=obj.content.split()
        if len(words)>10:
            truncated_content=' '.join(words[:10])+ '...'
        else:
            truncated_content=' '.join(words)
        
        return truncated_content
    
    
    truncated_summary.short_description = 'summary'
    truncated_content.short_description = 'content'
    
class CustomUserAdmin(UserAdmin):
    list_display=['username', 'email', 'is_active', 'is_staff', 'is_superuser']


try:
    admin.site.register(UserProfile, CustomUserAdmin)
except admin.sites.AlreadyRegistered:
    pass

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor','patient','required_speciality', 'date_of_appointment', 'start_time', 'end_time']

