# Generated by Django 4.2.2 on 2024-09-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_client_owner_mailing_is_active_mailing_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
    ]
