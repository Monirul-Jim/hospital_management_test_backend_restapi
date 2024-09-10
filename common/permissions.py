from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework import status

class IsAuthenticatedCustom(BasePermission):
    message={
        "success":False,
        "message":'unauthorize',
        "errorSources":[
          {  
           "path":"",
           "message":"unauthorize"
           }
            
        ],
        "err":{
            "statusCode":401
        }
    }
    def has_permission(self,request,view):
        if not request.user or not request.user.is_authenticated:
            return False
        return True
    def permission_denied(self,request, message=None):
        return Response(self.message, status=status.HTTP_401_UNAUTHORIZED)
