from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name="landing"),
	url(r'register$', views.register, name="register"),
	url(r'login$', views.login, name="login"),
	url(r'pokes$', views.dashboard, name="dashboard"),
	url(r'logout$', views.logout, name="logout"),
	url(r'^pokes/(?P<user_id>\d+)/$', views.poke, name="poke")
]