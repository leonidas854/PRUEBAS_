from django.urls import path
from.views import resolver_nqueens



urlpatterns = [
    path('resolver/<int:n>/',resolver_nqueens,name='resolver_nqueens'),

]