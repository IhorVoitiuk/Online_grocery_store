# Generated by Django 4.2.1 on 2023-05-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttranslation',
            name='mini_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
