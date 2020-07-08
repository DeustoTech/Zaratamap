# Generated by Django 2.2.6 on 2020-06-04 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zaratamap_app', '0015_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='profile_picture',
            field=models.ImageField(default='media\\profile_pictures\\profileDog.jpg', upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='profilepicture',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]