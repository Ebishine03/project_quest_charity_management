# Generated by Django 5.0.2 on 2024-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_customuser_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_img',
            field=models.ImageField(blank=True, upload_to='user_image'),
        ),
    ]
