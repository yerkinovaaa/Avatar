# Generated by Django 4.0.3 on 2022-04-29 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name Surname', max_length=200, null=True)),
                ('title', models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey, there this a default text description about you that you can change on after clicking on "Edit" or going', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
