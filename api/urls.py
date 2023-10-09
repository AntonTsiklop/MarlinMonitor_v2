from django.urls import path
from .views import AT500Updater

urlpatterns = [
    path('v1/update_AT500', AT500Updater.as_view()),
]