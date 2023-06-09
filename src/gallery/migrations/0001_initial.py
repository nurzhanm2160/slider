# Generated by Django 4.2 on 2023-04-15 09:45

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
                ('image', models.ImageField(upload_to='uploads/', verbose_name='Изображение')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления изображения')),
            ],
            options={
                'verbose_name': 'Изоброжение',
                'verbose_name_plural': 'Изоброжении',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Галлерея', max_length=255, verbose_name='Название галлереи')),
                ('image', models.ImageField(upload_to='uploads/', verbose_name='Главная картинка')),
                ('images', models.ManyToManyField(to='gallery.image')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлерея',
            },
        ),
    ]
