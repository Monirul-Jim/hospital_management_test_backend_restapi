from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from rest_framework import status

class IsAuthenticatedCustomMiddleware(MiddlewareMixin):
    custom_message = {
        "success": False,
        "message": 'unauthorize',
        "errorSources": [
            {
                "path": "",
                "message": "unauthorize"
            }
        ],
        "err": {
            "statusCode": status.HTTP_401_UNAUTHORIZED
        }
    }

    # Define the paths that should not require authentication
    EXCLUDED_PATHS = ['/patient/login/', 'patient/register/', '/admin/',]

    def process_request(self, request):
        # Get the current request path
        current_path = request.path_info
        
        # Check if the current path is in the excluded paths
        if current_path in self.EXCLUDED_PATHS:
            return None  # Allow access without authentication
        
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Return the custom response for unauthenticated users
            return JsonResponse(self.custom_message, status=401)
        
        # Return None to continue processing the request
        return None
