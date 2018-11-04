from django.urls import path
from .views import ListAllEventsView
from .views import CreateEventView
from.views import RetrieveDestroyEventView


urlpatterns = [
    path('', CreateEventView.as_view(), name="create"),  # Post to root url
    path('all/', ListAllEventsView.as_view(), name="events-all"),
    path('<int:pk>', RetrieveDestroyEventView.as_view(), name='events-retrievedestroy')
]
