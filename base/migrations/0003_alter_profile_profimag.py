# Generated by Django 4.2.5 on 2024-01-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_name_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profimag',
            field=models.ImageField(default='avatar.png', upload_to='prof_images'),
        ),
    ]