# Generated by Django 5.0.6 on 2024-09-17 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jvs_app', '0006_offerimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerimages',
            name='Offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offer_images', to='jvs_app.offer'),
        ),
    ]
