# Generated by Django 2.2 on 2019-04-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0005_auto_20190423_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='komentaz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.Kategoria'),
        ),
    ]
