# Generated by Django 5.0.6 on 2024-09-10 10:14

import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jvs_app', '0003_product_featured_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=6, max_length=30, prefix='CAT-'),
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1233, upload_to='Product_image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pid',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=6, max_length=30, prefix='PRD-'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='jvs_app.category'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='prd.jpg', upload_to='Product_images/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jvs_app.product')),
            ],
        ),
    ]
