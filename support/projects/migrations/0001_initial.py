# Generated by Django 3.1.3 on 2020-11-18 20:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reglogin', '0002_auto_20201118_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('target', models.FloatField()),
                ('created_at', models.DateField(verbose_name=datetime.datetime(2020, 11, 18, 20, 34, 8, 394185, tzinfo=utc))),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('images', models.ImageField(upload_to='')),
                ('total_rate', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.users')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.users')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.FloatField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.users')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=500)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.users')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.CharField(max_length=500)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.comments')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.users')),
            ],
        ),
    ]