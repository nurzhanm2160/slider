from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='uploads/')
    uploaded_time = models.DateTimeField('Дата добавления изображения', auto_now_add=True)

    class Meta:
        verbose_name = 'Изоброжение'
        verbose_name_plural = 'Изоброжении'

    def __str__(self):
        return self.image.name


class Gallery(models.Model):
    name = models.CharField('Название галлереи', max_length=255, default='Галлерея')
    image = models.ImageField('Главная картинка', upload_to='uploads/')
    images = models.ManyToManyField(Image)

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

    def __str__(self):
        return self.name
