from rest_framework import serializers
from contact_us.models import ContactModel

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields='__all__'