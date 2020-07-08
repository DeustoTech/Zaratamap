# Generated by Django 2.2.6 on 2020-05-14 05:29

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zaratamap_app', '0006_auto_20200514_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='vehicles',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filter',
            name='km_dec',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='km_int',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='lat_dec',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='lat_int',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='lon_dec',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='lon_int',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
