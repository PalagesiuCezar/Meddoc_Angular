from rest_framework import permissions

class IsDoctorOrNot(permissions.BasePermission):
    message = 'You are not allowed here because you are not a Doctor'

    def has_object_permission(self,request,view,obj):
        return obj.is_doctor == request.user

        
