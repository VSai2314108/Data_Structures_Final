from rest_framework.serializers import ModelSerializer
from .models import Out

class OutSerializer(ModelSerializer):
    class Meta:
        model = Out
        fields = '__all__'