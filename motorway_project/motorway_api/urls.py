from django.urls import path
from .views import ListAllEventsView
from .views import CreateFilterView
from.views import RetrieveDestroyEventView


urlpatterns = [
    path('', CreateFilterView.as_view(), name="create-filter"),  # Post to root url
    path('all/', ListAllEventsView.as_view(), name="events-all"),
    path('<int:pk>', RetrieveDestroyEventView.as_view(), name='events-retrievedestroy')
]
