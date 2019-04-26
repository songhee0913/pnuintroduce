from django.urls import path
from . import views

app_name = 'introduce'

urlpatterns = [
    path('', views.introduce_list),
    path('<int:pk>/', views.introduce_detail),
]
