from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth import get_user_model

from user.manager import UserManager
from django.contrib.auth.hashers import make_password, check_password

from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
	first_name = models.CharField(_('First Name') , max_length = 50, null=True, blank=True)
	last_name = models.CharField(_('Last Name') , max_length=50, null=True, blank=True)
	email = models.EmailField(_('Email Address') , unique=True)
	username = models.CharField(_('Username'), max_length=500, null=True, blank=True)
	password = models.CharField(_('Password'), max_length=200, null=True, blank=True)
	address = models.TextField(_('Address'), null=True, blank=True)
	city = models.CharField(_('City'), max_length=30, null=True, blank=True)
	state = models.CharField(_('State'), max_length=30, null=True, blank=True)
	country = models.CharField(_('Country'), max_length=30, null=True, blank=True)
	time_zone = models.CharField(_('Time Zone'), max_length=100, null=True, blank=True)
	time_zone_sub = models.CharField(_('Time Zone2'), max_length=300, null=True, blank=True)
	last_login = models.DateTimeField(_('Last Login'), null=True)
	first_login = models.DateTimeField(_('First Login'), null=True)
	login_count = models.IntegerField(_('Login Count'), null=True)
	active = models.BooleanField(_('User Active'), default=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	def check_password(self, raw_password):
		return check_password(raw_password, self.password)

	def hash_password(self, raw_password):
		hash_password = make_password(raw_password)
		return hash_password

	def save(self, *args, **kwargs):
		self.username = self.email
		super(User, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.email)

@receiver(post_save, sender=User)
def create_hashed_password(sender, instance=None, created=False, **kwargs):
	if created:
		hash_password = make_password(instance.password)
		user = User.objects.filter(id=instance.id).first()
		user.password = hash_password
		user.save()