from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.SerialListView.as_view(), name='series'),
    path('series/<int:pk>', views.SerialDetailView.as_view(), name='serial-detail'),
    path('directors/', views.DirectorListView.as_view(), name='directors'),
    path('genres/', views.GenresListView.as_view(), name='genres'),
    path('series/create/', views.SerialCreate.as_view(), name='serial-create'),
    path('series/<int:pk>/update/', views.SerialUpdate.as_view(), name='serial-update'),
    path('series/<int:pk>/delete/', views.SerialDelete.as_view(), name='serial-delete'),
    path('genres/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),
    path('directors/create/', views.DirectorCreate.as_view(), name='director-create'),
    path('directors/<int:pk>/update/', views.DirectorUpdate.as_view(), name='director-update'),
    path('directors/<int:pk>/delete/', views.DirectorDelete.as_view(), name='director-delete'),
]
