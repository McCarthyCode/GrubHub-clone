from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_restaurants, name="restaurant_home"),
    url(r'(?P<rest_id>\d+)$', views.rest_profile, name="rest_profile"),
    url(r'update_location$', views.update_location),
    url(r'delete_location$', views.destroy_location),
    url(r'(?P<rest_id>\d+)$', views.rest_profile, name="rest_profile"),
    url(r'add_restaurant$', views.add_restaurant, name="add_restaurant"),
    url(r'add_location$', views.add_location, name="add_location"),
    url(r'update_restaurant$', views.update_restaurant, name="update_restaurant"),
    url(r'delete_restaurant$', views.destroy_restaurant, name="destroy_restaurant"),
]
