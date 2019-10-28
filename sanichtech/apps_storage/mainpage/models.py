from django.db import models


''' -------------------------------------- Модель для главной страницы ----------------------- '''


class MainPage(models.Model):
    """ ------------- Модель для описания "О нас" """

    AboutUs_ru = models.TextField('О нас, рус', blank=False)
    AboutUs_ukr = models.TextField('О нас, укр', blank=False)
    AboutUs_en = models.TextField('О нас, англ', blank=False)
    AboutUs_de = models.TextField('О нас, нем', blank=False)

    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class MainPhotos(models.Model):
    """ ------------- Модель для картинок "О нас" """

    add_main_media = models.ForeignKey(MainPage, on_delete=models.CASCADE)
    MainPhoto = models.ImageField('Изображение для главной страницы', upload_to='media/photos/mainphotos')

    class Meta:
        verbose_name = 'Картинки для главной'
        verbose_name_plural = 'Картинки для главной'

    def __str__(self):
        return self.MainPhoto.name.lstrip(r'media/photos/mainphotos/')

