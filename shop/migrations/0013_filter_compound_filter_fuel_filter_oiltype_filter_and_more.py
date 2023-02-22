# Generated by Django 4.1.7 on 2023-02-22 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='compound',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
        migrations.AddField(
            model_name='fuel',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
        migrations.AddField(
            model_name='oiltype',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
        migrations.AddField(
            model_name='transmission',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
        migrations.AddField(
            model_name='vehicletype',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
        migrations.AddField(
            model_name='viscosity',
            name='filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.filter'),
        ),
    ]
