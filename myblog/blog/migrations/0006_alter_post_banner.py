# Generated by Django 5.1 on 2024-09-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='default.png', upload_to='media/'),
        ),
    ]
