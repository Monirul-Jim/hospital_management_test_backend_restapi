from rest_framework.routers import DefaultRouter
from django.urls import path, include
from patient.views import activate, PatientViewSets, UserLoginApiView, UserRegistrationViews,UserLogoutView

router = DefaultRouter()
router.register('patient', PatientViewSets)
urlpatterns=[
    path('patients/',include(router.urls)),
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/',activate, name='activate'),
]