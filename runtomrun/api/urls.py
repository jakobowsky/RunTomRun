from django.urls import path

from . import views

urlpatterns = [
    path('<x>/<y>/<radius>/<length>/', views.index, name='generate'),
]