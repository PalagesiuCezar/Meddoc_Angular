from django.urls import path
from .views import index
from django.urls import path
from django.conf.urls import url

from knox import views as knox_views

from .views import ( RegisterView,UserViewSet, 
LoginView,PacientView,DoctorView,AppointmentView)

user_routes = [
    (r'users', UserViewSet),
]

profile_routes = [
    (r'pacient',PacientView),
    (r'doctor',DoctorView),
    (r'appointment',AppointmentView),
]

urlpatterns = [
    path('muie/', index.as_view()),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', knox_views.LogoutView.as_view(), name="knox_logout"),
    # path('app/',AppointmentView.as_view(),name="app"),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]