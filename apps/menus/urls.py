from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.menu_profile, name="menu_home"),
    url(r'^create_menu$', views.create_menu, name="create_menu"),
    url(r'^update_menu$', views.update_menu, name="update_menu"),
    url(r'^destroy_menu/(?P<menu_id>\d+)$', views.destroy_menu, name="destroy_menu"),
    url(r'^create_item$', views.create_item, name="create_item"),
]
