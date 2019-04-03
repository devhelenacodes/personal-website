from django.http import HttpResponse
from django.conf.urls import include, url
from django.shortcuts import render
from . import views
# Create your views here.
#def post_home(request):
#	return HttpResponse("<h1>Hello</h1>")

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^create/$', views.post_create),
	url(r'^detail/$', views.post_detail),
	url(r'^update/$', views.post_update),
	url(r'^delete/$', views.post_delete),
]
'''
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
#    url(r'posts/$', post_home),
    path('admin/', admin.site.urls),
    
]
'''