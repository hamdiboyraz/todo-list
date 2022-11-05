from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'), #url:update_task/2
    path('delete/<str:pk>/', views.deleteTask, name='delete_task'), #url: delete/2
]