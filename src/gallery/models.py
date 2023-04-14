from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='uploads/% Y/% m/% d/')
    uploaded_time = models.DateTimeField('Дата добавления изображения', auto_now_add=True)

    class Meta:
        verbose_name = 'Изоброжение'
        verbose_name_plural = 'Изоброжении'

    def __str__(self):
        return self.image


class Gallery(models.Model):
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

    def __str__(self):
        return self.images
