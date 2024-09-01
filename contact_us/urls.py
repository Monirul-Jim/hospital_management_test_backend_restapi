from rest_framework.routers import DefaultRouter
from django.urls import path,include
from contact_us.views import ContactUsViewSet

router=DefaultRouter()
router.register('contact-us',ContactUsViewSet,)
urlpatterns=[
    path('',include(router.urls)),
]