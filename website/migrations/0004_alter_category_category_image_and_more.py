# Generated by Django 4.2.3 on 2023-07-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20230526_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
