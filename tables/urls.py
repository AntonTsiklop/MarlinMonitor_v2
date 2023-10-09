from django.urls import path
from .views import *

app_name = 'tables'
urlpatterns = [
    path('', main, name='main'),
    path('track', track, name='track'),
    path('permafrost', permafrost, name='permafrost')
]