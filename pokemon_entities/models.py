from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название покемона')
    image = models.ImageField(
        upload_to='',
        default=None,
        verbose_name='Изображение'
    )
    description = models.TextField(
        max_length=1024, null=False, blank=True, default='',
        verbose_name='Описание'
    )
    title_en = models.CharField(
        max_length=200, null=False, blank=True, default='',
        verbose_name='Английское название'
    )
    title_jp = models.CharField(
        max_length=200, null=False, blank=True, default='',
        verbose_name='Японское название'
    )
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='next_evolution',
        verbose_name='Из кого эволюционирует'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.PROTECT,
        related_name='entities',
        verbose_name='Название покемона'
    )
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        blank=True, null=True,
        verbose_name='Появился'
    )
    dissapeared_at = models.DateTimeField(
        blank=True, null=True,
        verbose_name='Исчез'
    )
    level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='ХП')
    strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    stamina = models.IntegerField(
        blank=True, null=True,
        verbose_name='Выносливость'
    )

    def __str__(self):
        return self.pokemon.title
