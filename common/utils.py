# common/utils.py

from django.http import JsonResponse
from rest_framework import status

# Custom 404 handler
def custom_not_found_page(request, exception=None):
    response = {
        "success": False,
        "message": "API Not Found !!",
        "error": "",
    }
    return JsonResponse(response, status=status.HTTP_404_NOT_FOUND)

# Custom 500 handler
def custom_server_error_page(request):
    response = {
        "success": False,
        "message": "Server Error !!",
        "error": "",
    }
    return JsonResponse(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



