# Generated by Django 3.1.2 on 2020-12-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_organization_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='compensation',
            field=models.CharField(default='1,000,000', max_length=20),
        ),
    ]
