from rest_framework import serializers
from leads.models import Lead

# Lead Serializer (turning Lead model into a Serializer)
# Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead # Designate the model to be serialized
        fields = '__all__' # Select all fields in the Lead model to include in the serializer

