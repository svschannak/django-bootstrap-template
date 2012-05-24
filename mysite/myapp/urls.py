from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.myapp.views',
    url(r'^$', 'home'),
)