from django.urls import path
from .views import suma, resta, multiplicacion, division

urlpatterns = [
    path('suma/', suma),
    path('resta/', resta),
    path('multiplicacion/', multiplicacion),
    path('division/', division),
]
