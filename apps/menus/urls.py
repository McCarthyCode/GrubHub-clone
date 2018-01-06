from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.menu_profile, name="menu_home"),
    url(r'^create_menu$', views.create_menu, name="create_menu"),
]
