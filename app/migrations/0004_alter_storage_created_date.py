# Generated by Django 5.0.4 on 2024-04-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]