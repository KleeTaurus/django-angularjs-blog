from django.conf.urls import patterns, url
import views


urlpatterns = patterns(
    '',
    url(r'^/blogs/?$', views.BlogPostListCreateAPIView.as_view(), name='blog_post_list_create'),
    url(r'^/blogs/(?P<pk>\d+)/?$', views.BlogPostInstanceAPIView.as_view(), name='blog_post_instance')
)
