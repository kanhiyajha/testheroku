from django.conf.urls import patterns, include, url
from polls.views import *
from django.contrib import admin
from django.conf import settings
#admin.autodiscover()
from polls.views import *

urlpatterns = patterns('',
                       url(r'^$',method),
                                             url(r'^setdata/',setdata),
                       url(r'^display/(?P<list1>.+)$',display),
                                             
)
