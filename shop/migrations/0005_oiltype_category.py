# Generated by Django 4.1.7 on 2023-02-21 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_transmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='oiltype',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
        ),
    ]
