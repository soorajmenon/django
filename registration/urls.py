

from django.conf.urls import include, url
from django.contrib import admin
from registration import views
from registration.views import *
from registration.models import *
from django.views.generic import TemplateView
from django.views.generic import ListView



urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='login.html'),
        name='page'),
    url(r'^chocolate/add/',AddChocolateView.as_view(), name="add_chocolate"),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='edit_profile'),
    url(r'^user/profile/edit/success', UserProfileUpdateView.as_view(template_name='success2.html'), name='edit_profile1'),


]





