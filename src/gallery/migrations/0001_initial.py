# Generated by Django 4.2 on 2023-04-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/% Y/% m/% d/', verbose_name='Изображение')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления изображения')),
            ],
        ),
    ]