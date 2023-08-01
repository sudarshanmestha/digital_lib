from django.urls import path
from . import views
from digital_lib.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-book'),
    path('<int:id>/update/', views.update_book, name='update-book'),
    path('<int:id>/delete/', views.delete_book, name='delete--book')
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)