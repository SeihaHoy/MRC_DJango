from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blog_post_list_create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blog_post_retrieve_update_destroy'),
    path('sensors/', views.SensorsListCreate.as_view(), name='sensors_list_create'),
    path('sensors/<int:pk>/', views.SensorsRetrieveUpdateDestroy.as_view(), name='sensors_retrieve_update_destroy'),
    path('sensordata/', views.SensorDataListCreate.as_view(), name='sensor_data_list_create'),
    path('sensordata/<int:pk>/', views.SensorDataRetrieveUpdateDestroy.as_view(), name='sensor_data_retrieve_update_destroy'),
]