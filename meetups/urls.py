from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('meetups/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail')
]