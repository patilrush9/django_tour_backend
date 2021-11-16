from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q as queue

from rest_framework.permissions import AllowAny

from django.template.loader import render_to_string

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework import parsers, exceptions

from user.models import *
from random import * 
from user.serializers import *

from tourapp.models import *
from tourapp.serializers import *

import json
import secrets
import string

from django.db import close_old_connections, connection

# from user.config.config import *

import datetime

# Create your views here.

class TripApiView(APIView):
	def post(self, request):
		if request.data:
			serializer = TourSerializerTest(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'message':'Tour Registered Successfully', 'status':True, 'status_code':200}, status=200)
			else:
				return JsonResponse({'message':'Error During Tour Registration', 'status':False, 'status_code':400, 'error':serializer.errors}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def get(self, request):
		tour_id = request.GET.get('id', None)
		if tour_id:
			Tour = tour.objects.filter(id=tour_id).all()
			serializer = TourReadSerializers(Tour, many=True)
			return JsonResponse({'message':'tour', 'status':True, 'status_code':200, 'Tour':serializer.data}, status=200)
		return JsonResponse({'message':'Tour not found', 'status':False, 'status_code':400}, status=400)

	def put(self, request):
		if request.data:
			tour_id = request.GET.get('id', None)
			Tour = tour.objects.filter(id=tour_id).last()
			if Tour:
				serializer = TourSerializerTest(Tour, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Tour Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Tour Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Tour', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def delete(self, request):
		tour = request.GET.get('id', None)
		if tour:
			Del = tour.objects.filter(id=tour).delete()
			return JsonResponse({"message":"Tour Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=40)





class GalleryView(APIView):
	def post(self, request):
		if request.data:
			serializer = GallerySerializerTest(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'message':'Image Registered Successfully', 'status':True, 'status_code':200}, status=200)
			else:
				return JsonResponse({'message':'Error During Image Registration', 'status':False, 'status_code':400, 'error':serializer.errors}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def get(self, request):
		glry_id = request.GET.get('id', None)
		if glry_id:
			Gallery = gallery.objects.filter(id=glry_id).all()
			serializer = GalleryReadSerializers(Gallery, many=True)
			return JsonResponse({'message':'Image', 'status':True, 'status_code':200, 'Tour':serializer.data}, status=200)
		return JsonResponse({'message':'Image not found', 'status':False, 'status_code':400}, status=400)

	def put(self, request):
		if request.data:
			glry_id = request.GET.get('id', None)
			Gallery = gallery.objects.filter(id=glry_id).last()
			if Gallery:
				serializer = GallerySerializerTest(Gallery, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Image Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Image Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Image', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def delete(self, request):
		glry_id = request.GET.get('id', None)
		if glry_id:
			Del = gallery.objects.filter(id=glry_id).delete()
			return JsonResponse({"message":"Image Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=40)


class EnquiryView(APIView):
	def post(self, request):
		if request.data:
			serializer = EnquirySerializerTest(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'message':'Enquiry Registered Successfully', 'status':True, 'status_code':200}, status=200)
			else:
				return JsonResponse({'message':'Error During Enquiry Registration', 'status':False, 'status_code':400, 'error':serializer.errors}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def get(self, request):
		en_id = request.GET.get('id', None)
		if en_id:
			Enquiry = enquiry.objects.filter(id=en_id).all()
			serializer = EnquiryReadSerializers(Enquiry, many=True)
			return JsonResponse({'message':'Enquiry', 'status':True, 'status_code':200, 'Enquiry':serializer.data}, status=200)
		return JsonResponse({'message':'Enquiry not found', 'status':False, 'status_code':400}, status=400)

	def put(self, request):
		if request.data:
			en_id = request.GET.get('id', None)
			Enquiry = enquiry.objects.filter(id=en_id).last()
			if Enquiry:
				serializer = EnquirySerializerTest(Enquiry, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Enquiry Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Enquiry Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Enquiry', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def delete(self, request):
		en_id = request.GET.get('id', None)
		if en_id:
			Del = enquiry.objects.filter(id=en_id).delete()
			return JsonResponse({"message":"Enquiry Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=40)