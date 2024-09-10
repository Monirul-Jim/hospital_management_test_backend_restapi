from rest_framework.routers import DefaultRouter
from doctor.views import DoctorViewSet
from django.urls import path,include
router = DefaultRouter()
router.register('doctor',DoctorViewSet)
urlpatterns=[
    path('doctors/',include(router.urls)),
    path('available-time/',include(router.urls))
] 