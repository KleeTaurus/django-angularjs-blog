from django.conf.urls import patterns, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', views.HomeView.as_view(), name='home')
)
