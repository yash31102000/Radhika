from django.urls import path
from .views import *
urlpatterns = [
     path("login/",LoginViewSet.as_view()),
     path("categories/",CategoryViewSet.as_view()),
     path("categories/<int:pk>/",CategoryGetViewSet.as_view()),
     path("items/",ItemViewSet.as_view()),
     path("items/<int:pk>/",ItemGetViewSet.as_view()),
     path("event-bookings/",EventBookingViewSet.as_view()),
     path("event-bookings/<int:pk>/",EventBookingGetViewSet.as_view()),
     path("eventfilter/",EventFilterViewSet.as_view()),
     path("stoke-items/",StokeItemViewSet.as_view()),
     path("stoke-items/<int:pk>/",EditStokeItemViewSet.as_view()),
     path("add-stoke-item/",AddRemoveStokeItemViewSet.as_view()),
     path("alert-stoke-item/",AlertstokeItemViewSet.as_view()),

]