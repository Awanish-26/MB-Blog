# Generated by Django 5.1 on 2024-09-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_banner_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
