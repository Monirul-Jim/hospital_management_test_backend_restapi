from rest_framework import viewsets
from patient.models import PatientModel
from patient.serializers import PatientSerializers ,UserRegistrationSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class PatientViewSets(viewsets.ModelViewSet):
    queryset=PatientModel.objects.all()
    serializer_class= PatientSerializers
    
    
class UserRegistrationViews(APIView):
    
    serializer_class = UserRegistrationSerializers
    
    
    def post(self,request):
        serializer = self.serializer_class(data =  request.data)

        
        if serializer.is_valid():
            user =serializer.save()
            print(user)
            return Response('Done')
        return Response(serializer.errors)