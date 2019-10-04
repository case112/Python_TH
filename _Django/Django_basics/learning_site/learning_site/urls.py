from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'learning_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^courses/', include('courses.urls', namespace='courses')), #it lets to include urls from other apps
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.hello_world),
]

urlpatterns += staticfiles_urlpatterns()