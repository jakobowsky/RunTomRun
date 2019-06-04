from django.urls import path

from . import views

urlpatterns = [
    path('<str:x>/<str:y>/<int:radius>/<int:length>/', views.index, name='generate'),
]