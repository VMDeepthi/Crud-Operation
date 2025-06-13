from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create'),
    path('update/<int:id>/', views.update_item, name='update'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
    path('view/<int:id>/', views.view_item, name='view'),
]
