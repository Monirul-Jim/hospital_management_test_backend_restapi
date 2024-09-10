"""
URL configuration for hospital_management_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from common.utils import custom_not_found_page,custom_server_error_page
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('contact/', include('contact_us.urls')),
  path('service/', include('service.urls')),
  path('patient/', include('patient.urls')),
  path('appointment/', include('appointment.urls')),
  path('doctor/', include('doctor.urls')),
    # ... other URL patterns here
]
handler404 = 'common.utils.custom_not_found_page'
handler500 = 'common.utils.custom_server_error_page'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)