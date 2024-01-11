from django.db import models

class Zapis(models.Model):
    FIO = models.CharField('ФИО', max_length=100)
    date_bith = models.DateField('Дата рождения')
    category = models.CharField('Категория врача', max_length=50)
    date = models.DateTimeField('Дата и время записи')
    number = models.IntegerField('Номер телефона')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Запись на прием'


class Vrahi(models.Model):
    FIO = models.CharField('ФИО', max_length=100)
    category = models.CharField('Категория врача', max_length=50)
    stag = models.CharField('Стаж работы', max_length=2)
    date = models.CharField('Дни работы', max_length=30)
    time = models.CharField('Часы работы', max_length=30)


    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'