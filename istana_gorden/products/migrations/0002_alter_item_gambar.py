# Generated by Django 5.0.3 on 2024-03-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gambar',
            field=models.ImageField(default='static/images/default.png', upload_to='items'),
        ),
    ]
