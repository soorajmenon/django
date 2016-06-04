

from django.conf.urls import include, url
from django.contrib import admin
from registration import views
from registration.views import *
from registration.models import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),
        name='page')

]





