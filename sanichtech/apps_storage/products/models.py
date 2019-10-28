from django.db import models


''' -------------------------------------- Модель для продуктов ----------------------- '''


def product_path_video(instance, filename):  # метод, который дает возможность забрать имя вызывающей таблицы
    return 'media/videos/products/{0}/{1}'.format(instance.ProductName_ru, filename)

class Product(models.Model):
    """ ------------- Модель для добавления данных о продукте """

    ProductName_ru = models.CharField('Имя продукта рус', max_length=100, blank=False)
    ProductDescription_ru = models.TextField('Описание продукта рус', blank=False)
    ProductVideo_ru = models.FileField('Видео рус', upload_to=product_path_video, blank=True)

    ProductName_ukr = models.CharField('Имя продукта укр', max_length=100, blank=False)
    ProductDescription_ukr = models.TextField('Описание продукта укр', blank=False)
    ProductVideo_ukr = models.FileField('Видео укр', upload_to=product_path_video, blank=True)

    ProductName_en = models.CharField('Имя продукта англ', max_length=100, blank=False)
    ProductDescription_en = models.TextField('Описание продукта англ', blank=False)
    ProductVideo_en = models.FileField('Видео англ', upload_to=product_path_video, blank=True)

    ProductName_de = models.CharField('Имя продукта нем', max_length=100, blank=False)
    ProductDescription_de = models.TextField('Описание продукта нем', blank=False)
    ProductVideo_de = models.FileField('Видео нем', upload_to=product_path_video, blank=True)

    class Meta:
        verbose_name_plural = 'Данные о продукте'

    def __str__(self):
        return self.ProductName_ru


def product_path_photo(instance, filename):  # метод, который дает возможность забрать имя вызывающей таблицы
    return 'media/photos/products/{0}/{1}'.format(instance.add_media.ProductName_ru, filename)

class AddFiles(models.Model):
    """ ------------- Модель для добавления медии о продуктах """

    add_media = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductPhoto = models.ImageField('Изображение продукта', upload_to=product_path_photo, blank=True)

    class Meta:
        verbose_name_plural = 'Картинки для продуктов'

    def __str__(self):
        return self.ProductPhoto.name.lstrip(r'media/photos/products/')

