from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='uploads/% Y/% m/% d/')

    def __str__(self):
        return self.image
