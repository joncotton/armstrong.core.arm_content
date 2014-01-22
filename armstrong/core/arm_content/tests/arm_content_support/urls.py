from django.contrib import admin
try:
    from django.conf.urls import patterns, include, url
except ImportError:  # Django 1.3
    from django.conf.urls.defaults import patterns, include, url


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
