from django.urls import path

from . import views

urlpatterns = [
    path('<x>/<y>/<length>/', views.index, name='generate'),
]