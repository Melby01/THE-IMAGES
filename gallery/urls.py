from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.image_of_day,name='imageToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_image,name = 'pastImage'),
    url(r'^search/', views.search_results, name='search_results'),
    url('image/<int:image_id>', views.view_image,name='view_image'),
    url(r'^$',views.index,name='index'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

