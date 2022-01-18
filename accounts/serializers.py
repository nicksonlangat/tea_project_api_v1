from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email','first_name','last_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):

        user = get_user_model().objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'team_leader','first_name','last_name', 'employee_number','date_employed']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['team_leader'] = instance.team_leader.first_name
        return representation