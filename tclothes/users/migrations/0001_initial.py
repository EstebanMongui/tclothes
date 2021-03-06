# Generated by Django 3.0.9 on 2020-08-30 21:50

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
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
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which object was last modified.', verbose_name='modified at')),
                ('username', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='The phone number must be entered in the format: 1234567890. With 10 digits.', regex='^[0-9]\\d{9}$')], verbose_name='user phone number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which object was created.', verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Date time on which object was last modified.', verbose_name='modified at')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='Profile picture')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='User city')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='User state')),
                ('last_super_like', models.DateTimeField(help_text='Date time when the user did him/her last SUPERLIKE.', null=True, verbose_name='Last SUPER-LIKE date')),
                ('remaining_clothes', models.PositiveSmallIntegerField(default=0, help_text='Solo puedes subir un total de 10 prendas.', validators=[django.core.validators.MaxValueValidator(limit_value=10)], verbose_name='Clothe pictures related')),
                ('is_profile_complete', models.BooleanField(default=False, help_text='Is true when all profile info are complete.', verbose_name='Profile complete')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
