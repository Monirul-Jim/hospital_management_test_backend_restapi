from rest_framework.routers import DefaultRouter
from appointment.views import AppointmentViewSet
from django.urls import path,include
router = DefaultRouter()
router.register('appointment', AppointmentViewSet)
urlpatterns=[
    path('appointments/',include(router.urls))
]