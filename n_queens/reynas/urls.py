from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('resolver/<int:n>/', views.resolver_nqueens, name='resolver_nqueens'),
]
