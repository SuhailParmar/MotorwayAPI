from django.urls import path
from .views import ListAllEventsView
from .views import CreateEventView


urlpatterns = [
    path('', CreateEventView.as_view(), name="create"),  # Post to root url
    path('all/', ListAllEventsView.as_view(), name="events-all")
]
