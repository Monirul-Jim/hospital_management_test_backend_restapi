from rest_framework import serializers
from patient.models import PatientModel
from django.contrib.auth.models import User
class PatientSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    class Meta:
        model = PatientModel
        fields = '__all__'
        
        
        
class UserRegistrationSerializers(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(required = True)

    # def validate_email(self,value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError({'error':'Email address already exists.'})
    #     return value
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']
        
    def save(self):
        username= self.validated_data['username']
        first_name= self.validated_data['first_name']
        last_name= self.validated_data['last_name']
        email= self.validated_data['email']
        password= self.validated_data['password']
        password2= self.validated_data['confirm_password']
        
        if password != password2 :
            raise serializers.ValidationError({'error':'Password Does Not Match'})
        
        if User.objects.filter(email= email).exists():
            raise serializers.ValidationError({'error':'Email Already Exists'})
        
        account = User(username = username , email = email, first_name= first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.save()
        return account