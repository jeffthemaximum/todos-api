from django.conf.urls import url
from .views import (
	Register,
        LoginView,
        CreateTodo,
        ViewAll,
        ViewUnfinished,
)
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
        url(r'^register$', csrf_exempt(Register.as_view()), name = 'register' ),
        url(r'^login$', csrf_exempt(LoginView.as_view()), name = 'login' ),
        url(r'^(?P<token>[a-f0-9]+)/create$', csrf_exempt(CreateTodo.as_view()), name ='create'),
	url(r'^(?P<token>[a-f0-9]+)/view-all$', csrf_exempt(ViewAll.as_view()), name='view-all'),
	url(r'^(?P<token>[\w]+)/unfinished$' ,csrf_exempt(ViewUnfinished.as_view()), name='unfinished'),
	# url(r'^(?P<token>[\w]+)/view_all$' ,views.all, name='all'),




]
