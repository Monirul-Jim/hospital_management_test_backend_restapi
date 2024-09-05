from rest_framework.routers import DefaultRouter
from django.urls import path, include
from patient.views import PatientViewSets , UserRegistrationViews
router = DefaultRouter()
router.register('patient', PatientViewSets)
urlpatterns=[
    path('patients/',include(router.urls)),
    path('register/', UserRegistrationViews.as_view(), name='register'),
]