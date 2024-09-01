from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service.views import ServicesViewSet


router=DefaultRouter()
router.register('services',ServicesViewSet)
urlpatterns=[
    path('service/', include(router.urls))
]