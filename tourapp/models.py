from django.db import models
from django.conf import settings

from datetime import datetime
import time

from tourapp.models import *

# Create your models here.

class tour(models.Model):
	tour_types = models.CharField(max_length = 50, null=True, blank=True)
	tour_names =  models.CharField(max_length = 50, null=True, blank=True)
	tour_short_description = models.TextField(max_length=100, null=True,blank=True)
	tour_long_descript = models.TextField(max_length=500, null=True,blank=True)
	tour_price =  models.CharField(max_length = 50, null=True, blank=True)
	tour_duration =  models.CharField(max_length = 50, null=True, blank=True)
	duartion_start_date = models.DateTimeField()
	duartion_end_date = models.DateTimeField()
	tour_location = models.CharField(max_length = 50, null=True, blank=True)
	latitude = models.CharField(max_length = 50, null=True, blank=True)
	longitude = models.CharField(max_length = 50, null=True, blank=True)
	total_seats = models.IntegerField(null=True, blank=True)
	booked_seat = models.IntegerField(null=True, blank=True)
	booking_start_date = models.DateTimeField()
	bookin_end_date = models.DateTimeField()

	def __str__(self):
		return self.tour_names



class gallery(models.Model):
	tour_id = models.ForeignKey(tour, on_delete=models.CASCADE, null=False)
	image = models.TextField(max_length=500, null=True, blank=True)



class enquiry(models.Model):
	first_name = models.CharField(max_length = 50, null=True, blank=True)
	middle_name = models.CharField(max_length = 50, null=True, blank=True)
	lastn_name = models.CharField(max_length = 50, null=True, blank=True)
	email_address = models.EmailField(null=True, blank=True)
	phone_number = models.CharField(max_length = 50, null=True, blank=True)
	date_of_birth = models.DateTimeField()
	passport_number = models.CharField(max_length = 50, null=True, blank=True)
	passport_expiration_date = models.DateTimeField()
	place_of_birth = models.CharField(max_length = 50, null=True, blank=True)
	nationality = models.CharField(max_length = 50, null=True, blank=True)
	credit_card_information = models.CharField(max_length = 50, null=True, blank=True)
	number = models.CharField(max_length = 50, null=True, blank=True)
	expiration = models.DateTimeField()
	cvv = models.CharField(max_length = 50, null=True, blank=True)
	address = models.CharField(max_length = 50, null=True, blank=True)
	city = models.CharField(max_length = 50, null=True, blank=True)
	state = models.CharField(max_length = 50, null=True, blank=True)
	zip = models.CharField(max_length=20, blank=True)
