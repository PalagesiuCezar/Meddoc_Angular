from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone

from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from Accounts.utils.filters import UserFilter
from .serializers import (RegisterSerializer,UserSerializer,
                        PacientSerializer,DoctorSerializer,AppointmentSerializer)
from .models import User,Pacient,Doctor,Appointment
from Accounts.utils.perminssions import IsDoctorOrNot
#to see if it works

class index(generics.GenericAPIView):
    permission_classes = [IsDoctorOrNot]
    def get(self,request):
        return HttpResponse("aaaaa")
##


class BaseRegisterView(generics.GenericAPIView):

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                _, token = AuthToken.objects.create(user)
                return Response({'user': serializer.data,
                                 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(BaseRegisterView):
    serializer_class = RegisterSerializer

class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_class = UserFilter
    serializer_class = UserSerializer

#Profile views
class PacientView(viewsets.ModelViewSet):
    lookup_field = 'user'
    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer

class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DetailDoctorView(generics.RetrieveAPIView):
    pass

#Appointments

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

'''
view for reciever and sender to see theyre appointment
dont know if it works
'''
# class RecvViewApp(generics.GenericAPIView):
#     serializer_class = AppointmentSerializer
    # 
    # def get(self,request):
    #     queryset = Appointment.objects.filter(reciever = request.user)
    #     return Response(queryset)