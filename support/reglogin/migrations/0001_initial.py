

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
                ('mobile_number', models.IntegerField(null=True)),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('Provider', models.CharField(choices=[('mail', 'email'), ('facebook', 'facebook')], max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('facebook_profile', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
