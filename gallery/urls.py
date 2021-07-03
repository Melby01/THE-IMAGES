from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.image_of_day,name='imageToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_image,name = 'pastImage')
]