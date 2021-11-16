from django.urls import path, re_path
from django.conf.urls import url

from tourapp.views import *
# from service.apis.webhook import webhook_braintree 

urlpatterns = [
	url(r'^tour$', TripApiView.as_view(), name='tour_crud'),
	url(r'^gallery$', GalleryView.as_view(), name='gallery_crud'),
	url(r'^enquiry$', EnquiryView.as_view(), name='enquiry_crud'),
]