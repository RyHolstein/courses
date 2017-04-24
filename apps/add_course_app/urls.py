from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^course_submit$', views.submit),
    url(r'^course/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^delete$', views.delete)
]
