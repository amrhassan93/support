# Generated by Django 3.1.3 on 2020-11-28 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='')),
                ('Provider', models.CharField(choices=[('mail', 'email'), ('facebook', 'facebook')], max_length=50)),
                ('country', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('facebook_profile', models.CharField(max_length=100, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_acive', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
