# Generated by Django 3.2.9 on 2021-11-30 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TEST_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=40, verbose_name='Кабинет')),
                ('comment', models.TextField(max_length=200, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Кабинеты',
                'verbose_name_plural': 'Кабинет',
                'ordering': ['room'],
            },
        ),
        migrations.CreateModel(
            name='TEST_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('tech_id', models.IntegerField(verbose_name='Тех. ID')),
                ('invent_id', models.CharField(max_length=20, verbose_name='Инвентарный ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('comment', models.TextField(max_length=200, verbose_name='Комментарий')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.test_2', verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
                'ordering': ['name', 'time_create'],
            },
        ),
    ]
