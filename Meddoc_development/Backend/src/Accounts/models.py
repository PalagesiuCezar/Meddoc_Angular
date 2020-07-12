from django.db import models
from django.contrib.auth.models import AbstractUser
from Accounts.utils.managers import UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from Accounts.utils import choices
from django.conf import settings
# Create your models here.
class User(AbstractUser):

    objects = UserManager()

    username = None
    email = models.EmailField(_('email address'), unique=True)

    phone = models.CharField(_('phone number'), max_length=31, null=True)

    last_online = models.DateTimeField(_('last online'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_pacient = models.BooleanField('pacient',default='True')
    is_doctor = models.BooleanField('doctor',default='False')

    def __str__(self):
        return str(self.email)

class Pacient(models.Model):
    
    class Meta:
        verbose_name = _('Pacient')
        verbose_name_plural = _('Pacients')
        ordering = ('cnp',)

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pacient')

    sex = models.CharField(max_length=25,choices=choices.SEX,default='3')

    cnp = models.CharField(unique=True,max_length=50,default="None")

    blood_transfuzion = models.BooleanField(default=True)

    profile_picture = models.ImageField(upload_to='images/profile_images_pacients',blank=True,null=True)
    buletin_picture = models.ImageField(upload_to='images/buletin_pacients',blank=True,null=True)
    
    analize = models.FileField(upload_to='pdf_pacient/',blank=True,null=True)
    
    caption = models.TextField(unique=False,blank=False,max_length=750,default="")

    def __str__(self):
        return '{} pacient'.format(self.user)

class Doctor(models.Model):

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')
        ordering = ('hospital',)

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='doctor')

    sex = models.CharField(max_length=25,choices=choices.SEX,default='3')

    hospital = models.CharField(max_length=50,choices=choices.HOSPITALS,default="5")
    department = models.CharField(max_length=60,choices=choices.DEPARTMENT,default="5")

    caption = models.TextField(unique=False,blank=False,max_length=750,default="")

    profile_picture = models.ImageField(upload_to='images/profile_images_doctors',blank=True,null=True)
    buletin_picture = models.ImageField(upload_to='images/buletin_doctors',blank=True,null=True)
    
    def __str__(self):
        return '{} doctor'.format(self.user)

class Appointment(models.Model):

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointment')
        ordering = ('hospital',)

    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(User,on_delete = models.CASCADE,related_name='reciever')

    hospital = models.CharField(max_length=50,choices=choices.HOSPITALS,default="5")
    department = models.CharField(max_length=60,choices=choices.DEPARTMENT,default="5")

    emergency_type = models.CharField(max_length = 30, choices=choices.TYPE,default="1")

    start_day = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    
    content = models.CharField(max_length = 250,default='')
