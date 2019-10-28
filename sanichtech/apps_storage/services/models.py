from django.db import models


''' -------------------------------------- Модель для услуг ----------------------- '''


def service_path_video(instance, filename):  # метод, который дает возможность забрать имя вызывающей таблицы
    return 'media/videos/services/{0}/{1}'.format(instance.ProjectName_ru, filename)

class Service(models.Model):
    """ ------------- Модель для добавления данных об услугах """

    ServiceName_ru = models.CharField('Имя услуги рус', max_length=100, blank=False)
    ServiceDescription_ru = models.TextField('Описание услуги рус', blank=False)
    ServiceVideo_ru = models.FileField('Видео рус', upload_to=service_path_video, blank=True)

    ServiceName_ukr = models.CharField('Имя услуги укр', max_length=100, blank=False)
    ServiceDescription_ukr = models.TextField('Описание услуги укр', blank=False)
    ServiceVideo_ukr = models.FileField('Видео укр', upload_to=service_path_video, blank=True)

    ServiceName_en = models.CharField('Имя услуги англ', max_length=100, blank=False)
    ServiceDescription_en = models.TextField('Описание услуги англ', blank=False)
    ServiceVideo_en = models.FileField('Видео англ', upload_to=service_path_video, blank=True)

    ServiceName_de = models.CharField('Имя услуги нем', max_length=100, blank=False)
    ServiceDescription_de = models.TextField('Описание услуги нем', blank=False)
    ServiceVideo_de = models.FileField('Видео нем', upload_to=service_path_video, blank=True)

    class Meta:
        verbose_name_plural = 'Данные об услугах'

    def __str__(self):
        return self.ServiceName_ru


def service_path_photo(instance, filename):  # метод, который дает возможность забрать имя вызывающей таблицы
    return 'media/photos/services/{0}/{1}'.format(instance.add_media.ServiceName_ru, filename)

class AddFiles(models.Model):
    """ ------------- Модель для добавления медии об услугах """

    add_media = models.ForeignKey(Service, on_delete=models.CASCADE)
    ServicePhoto = models.ImageField('Изображение услуги', upload_to=service_path_photo, blank=True)

    class Meta:
        verbose_name_plural = 'Картинки для услуг'

    def __str__(self):
        return self.ServicePhoto.name.lstrip(r'media/photos/services/')
