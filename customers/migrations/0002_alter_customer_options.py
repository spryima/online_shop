# Generated by Django 4.2.7 on 2023-11-15 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={"verbose_name": "customer"},
        ),
    ]
