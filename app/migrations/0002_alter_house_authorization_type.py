# Generated by Django 5.0.4 on 2024-04-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='authorization_type',
            field=models.PositiveIntegerField(choices=[(1, 'Белая книга'), (2, 'Зеленая книга'), (3, 'Красная книга'), (4, 'Для аренды')]),
        ),
    ]
