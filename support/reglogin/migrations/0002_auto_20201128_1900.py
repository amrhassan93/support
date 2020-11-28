# Generated by Django 3.1.3 on 2020-11-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_acive',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='users',
            name='Provider',
            field=models.CharField(choices=[('mail', 'email'), ('facebook', 'facebook')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
    ]
