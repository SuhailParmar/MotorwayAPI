from django.urls import path
from .views import ListAllEventsView


urlpatterns = [
    path('all/', ListAllEventsView.as_view(), name="events-all")
]
