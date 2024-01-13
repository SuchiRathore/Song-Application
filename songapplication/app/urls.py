from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   # path('',views.index, name='index'),
   
    path('',views.songlist, name='songlist'),
    path('add/', views.addsong, name='addsong'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.updateview, name='update'),
    path('updatesong/', views.update, name='update_song'),
    path('play/<int:pk>/', views.playsong, name='play'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)