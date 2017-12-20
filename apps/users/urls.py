from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^lets-eat$', views.show_profile, name='lets_eat'),
    url(r'^account$', views.show_account, name='main_profile'),
    url(r'^account/update_name$', views.update_name),
    url(r'^account/update_email$', views.update_email),
    url(r'^account/update_password$', views.update_password),
    url(r'^account/address$', views.show_addresses, name='user_addresses'),
    url(r'^account/add_address$', views.add_address, name='add_address'),
    url(r'^account/update_address$', views.update_address, name='add_address'),
    url(r'^account/(?P<address_id>\d+)/destroy$', views.destroy_address),
    url(r'^reset$', views.reset, name='reset'),
]
