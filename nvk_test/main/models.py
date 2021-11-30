from django.db import models

# Create your models here.


class TEST_1(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    tech_id = models.IntegerField(verbose_name="Тех. ID")
    invent_id = models.CharField(max_length=20, verbose_name="Инвентарный ID")
    room = models.ForeignKey('TEST_2', on_delete=models.PROTECT, verbose_name="Кабинет")
    description = models.TextField(verbose_name="Описание")
    comment = models.TextField(max_length=200, verbose_name="Комментарий")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время последнего изменения")

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'
        ordering = ['name', 'time_create']

    def __str__(self):
        return self.name


class TEST_2(models.Model):
    room = models.CharField(max_length=40, verbose_name='Кабинет')
    comment = models.TextField(max_length=200, verbose_name='Комментарий')

    def __str__(self):
        return str(self.room)

    class Meta:
        verbose_name = "Кабинеты"
        verbose_name_plural = "Кабинет"
        ordering = ['room']