from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_restaurants, name="restaurant_home"),
    url(r'/(?P<rest_id>\d+)$', views.rest_profile, name="rest_profile"),
    url(r'add_restaurant$', views.add_restaurant),
    url(r'add_location$', views.add_location),
]
