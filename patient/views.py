from rest_framework import viewsets
from patient.models import PatientModel
from patient.serializers import (PatientSerializers, UserLoginSerializers,
    UserRegistrationSerializers)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

# email sending
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render , redirect


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
            token = default_token_generator.make_token(user)
            print('Token =',token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('Uid',uid)
            confirm_link = f'http://127.0.0.1:8000/patient/active/{uid}/{token}'
            print('confirm_link = ',confirm_link)
            email_subject = 'Confirm Your Email'
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to={user.email})
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response('Check your mail for confirmation')
        return Response(serializer.errors)
def activate(request, uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except(User.DoesNotExists):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class UserLoginApiView(APIView):
    def post(self,request):
        serializer = UserLoginSerializers(data =self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user =authenticate(username = username, password = password)
            
            if user:
                token , _ = Token.objects.get_or_create(user = user)
                login(request,user)
                return Response({'token' : token.key,'user_id':user.id})
            else:
                return Response({'error':'Invalid Credential'})
            
        return Response(serializer.errors)

class UserLogoutView(APIView):
     def get(self, request):
         request.user.auth_token.delete()
         logout(request) 
         return redirect('login') 
    