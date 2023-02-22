# Generated by Django 4.1.7 on 2023-02-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_vehicletype_category_compounds_category_fuels_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='compounds',
            field=models.ManyToManyField(blank=True, to='shop.compound'),
        ),
        migrations.AlterField(
            model_name='category',
            name='fuels',
            field=models.ManyToManyField(blank=True, to='shop.fuel'),
        ),
        migrations.AlterField(
            model_name='category',
            name='oiltypes',
            field=models.ManyToManyField(blank=True, related_name='oilset', to='shop.oiltype'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='transmissions',
            field=models.ManyToManyField(blank=True, to='shop.transmission'),
        ),
        migrations.AlterField(
            model_name='category',
            name='vehicle_types',
            field=models.ManyToManyField(blank=True, to='shop.vehicletype'),
        ),
        migrations.AlterField(
            model_name='category',
            name='viscosities',
            field=models.ManyToManyField(blank=True, to='shop.viscosity'),
        ),
    ]
