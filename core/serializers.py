from rest_framework import serializers
from .models import TeaWeight

class TeaWeightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeaWeight
        fields = ['id', 'employee','weight','entry_date']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['employee'] = instance.employee.employee_number
        return representation