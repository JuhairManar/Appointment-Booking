from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta, datetime, time
from .manage import *

# Create your models here.


class UserProfile(AbstractUser):
    username =models.CharField(max_length=255, unique=True, primary_key=True)
    email =models.EmailField(unique=True)
    profile_picture =models.ImageField(upload_to='profile_pictures/')
    address_line1 =models.CharField(max_length=100)
    city =models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    pincode =models.CharField(max_length=10)
    title =models.CharField(max_length=10)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

class Blog(models.Model):
    
    CATEGORIES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    )
    
    userprofile=models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blogs')
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='blog_images')
    category=models.CharField(choices=CATEGORIES, max_length=50)
    summary=models.TextField()
    content=models.TextField() 
    save_as_draft=models.BooleanField()
    
class Appointment(models.Model):
    SPECIALIZATIONS = (
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Endocrinology', 'Endocrinology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Hematology', 'Hematology'),
    )
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='doctor')
    required_speciality = models.CharField(max_length=50, choices=SPECIALIZATIONS)
    date_of_appointment = models.DateField(default=datetime.now().date() + timedelta(days=1))
    start_time = models.TimeField(default=time(8, 0))
    end_time = models.TimeField()

    @staticmethod
    def get_next_7_days():
        today = timezone.now().date()
        next_7_days = [(today + timedelta(days=i), today + timedelta(days=i)) for i in range(7)]
        return next_7_days

    @staticmethod
    def get_start_time_choices():
        start_time = time(hour=8, minute=0)  # Start time at 8:00 AM
        end_time = time(hour=21)  # End time at 9:00 PM
        interval = timedelta(minutes=45)  # 45 minutes interval
        choices = []
        current_time = start_time
        while current_time < end_time:
            choices.append((current_time.strftime('%H:%M'), current_time.strftime('%H:%M')))
            current_time = (datetime.combine(datetime.today(), current_time) + interval).time()
        return choices

# Set choices for date_of_appointment and start_time fields
Appointment.date_of_appointment.choices = Appointment.get_next_7_days()
Appointment.start_time.choices = Appointment.get_start_time_choices()