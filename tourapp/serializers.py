from rest_framework import serializers

from tourapp.models import *
from django.conf import settings

class TourSerializerTest(serializers.ModelSerializer):
	class Meta:
		model = tour
		fields = '__all__'


class TourReadSerializers(serializers.ModelSerializer):
	class Meta:
		model = tour
		fields = '__all__'


class GallerySerializerTest(serializers.ModelSerializer):
	class Meta:
		model = gallery
		fields = '__all__'

class GalleryReadSerializers(serializers.ModelSerializer):
	class Meta:
		model = gallery
		fields = '__all__'


class EnquirySerializerTest(serializers.ModelSerializer):
	class Meta:
		model = enquiry
		fields = '__all__'



class EnquiryReadSerializers(serializers.ModelSerializer):
	class Meta:
		model = enquiry
		fields = '__all__'