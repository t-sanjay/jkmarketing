from django.conf.urls import include, url 
from tutorials import views 
from django.contrib import admin

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'^api/getUsers$', views.tutorial_list),
    url(r'^api/getUsers/(?P<pk>[0-9]+)/(?P<zip_code>[0-9]+)$', views.getUsers)
]