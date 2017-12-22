from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<menu_type>[-\w\d]+)$', views.menu_profile, name="menu_home"),
]
