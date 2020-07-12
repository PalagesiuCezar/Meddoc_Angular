from django.contrib.auth import authenticate
import logging

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User,Pacient,Doctor,Appointment

from utils.serializers import DynamicFieldsModelSerializer
from utils.functions import exclude_fields

logger = logging.getLogger(__name__)


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','phone','password','is_pacient','is_doctor')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        user = User.objects.create_user(validated_data['email'], password=validated_data['password'],
                                        **exclude_fields(validated_data, exclude=('email', 'password')))
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')

class PacientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacient
        fields = '__all__' 
        # ordering = ('user','cnp',)

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'