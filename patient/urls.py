from rest_framework.routers import DefaultRouter
from django.urls import path, include
from patient.views import activate, PatientViewSets, UserRegistrationViews
from . import views
router = DefaultRouter()
router.register('patient', PatientViewSets)
urlpatterns=[
    path('patients/',include(router.urls)),
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
]