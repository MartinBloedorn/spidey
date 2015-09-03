from django.conf.urls import url
from spidey_rest import views


urlpatterns = [
    url(r'^$', views.spidey_main),
]
