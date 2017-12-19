from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^lets-eat$', views.show_profile, name='profile'),
    url(r'^account$', views.show_account, name='main_profile'),
    url(r'^account/address$', views.show_addresses, name='user_addresses'),
    url(r'^reset$', views.reset, name='reset'),
    url(r'^profile/address$', views.address, name='address'),
]
