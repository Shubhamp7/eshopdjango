# Generated by Django 3.0.6 on 2021-04-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_productkeys'),
    ]

    operations = [
        migrations.AddField(
            model_name='productkeys',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]