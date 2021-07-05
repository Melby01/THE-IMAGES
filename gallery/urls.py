from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^search/', views.search_results, name='search_results'),
    url('gallery/<int:gallery_id>', views.view_image,name='view_image'),
    url(r'^$',views.index,name='index'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

