# Generated by Django 2.2.10 on 2020-04-25 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(max_length=31, null=True, verbose_name='phone number')),
                ('last_online', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last online')),
                ('is_pacient', models.BooleanField(default='True', verbose_name='pacient')),
                ('is_doctor', models.BooleanField(default='False', verbose_name='doctor')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('2', 'Prefer not to say...')], default='Prefer not to say...', max_length=25)),
                ('cnp', models.CharField(default='None', max_length=50, unique=True)),
                ('blood_transfuzion', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/profile_images_pacients')),
                ('buletin_picture', models.ImageField(blank=True, null=True, upload_to='images/buletin_pacients')),
                ('analize', models.FileField(blank=True, null=True, upload_to='pdf_pacient/')),
                ('caption', models.TextField(default='', max_length=750)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pacient',
                'verbose_name_plural': 'Pacients',
                'ordering': ('cnp',),
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('2', 'Prefer not to say...')], default='Prefer not to say...', max_length=25)),
                ('hospital', models.CharField(default='None', max_length=50)),
                ('adress_hospital', models.CharField(default='None', max_length=60)),
                ('caption', models.TextField(default='', max_length=750)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/profile_images_doctors')),
                ('buletin_picture', models.ImageField(blank=True, null=True, upload_to='images/buletin_doctors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
                'ordering': ('hospital',),
            },
        ),
    ]
