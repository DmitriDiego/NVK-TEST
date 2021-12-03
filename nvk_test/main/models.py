from django.db import models


# Create your models here.


class Inv(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    tech_id = models.IntegerField(verbose_name="Тех. ID")
    invent_id = models.CharField(max_length=20, verbose_name="Инвентарный ID")
    room = models.ForeignKey('Room', on_delete=models.PROTECT, verbose_name="Кабинет")
    description = models.TextField(verbose_name="Описание")
    comment = models.TextField(max_length=200, verbose_name="Комментарий")
    department = models.ForeignKey('Dep', on_delete=models.PROTECT, verbose_name="Отдел")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время последнего изменения")

    #username = models.ForeignKey('auth_user', on_delete=models.PROTECT, verbose_name='Создавший пользователь')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'
        ordering = ['name', 'time_create']

    def __str__(self):
        return self.name


class Room(models.Model):
    room = models.CharField(max_length=40, verbose_name='Кабинет')
    comment = models.TextField(max_length=200, verbose_name='Комментарий')
    department = models.ForeignKey('Dep', on_delete=models.PROTECT, verbose_name='Отдел')

    def __str__(self):
        return str(self.room)

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ['department', 'room']


class Dep(models.Model):
    name = models.CharField(max_length=40, verbose_name="Отдел")

    class Meta:
        ordering = ["name"]
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Rep(models.Model):
    comment = models.TextField(max_length=200, verbose_name='Комментарий')
    inv = models.ForeignKey('Inv', on_delete=models.PROTECT, verbose_name='Оборудование')
    bool = models.BooleanField(default=False)

    class Meta:
        ordering = ["bool"]
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонты'

    def __str__(self):
        return str(self.inv)
