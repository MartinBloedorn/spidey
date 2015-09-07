from django.conf.urls import url
from spidey_rest import views


urlpatterns = [
    url(r'^$', views.spidey_main),
    url(r'^(?P<post_id>[0-9]+)/$', views.spidey_full_post),
]
