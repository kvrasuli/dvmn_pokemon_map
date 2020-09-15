from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    title_en = models.CharField(max_length=200, null=True, blank=True, default='')
    title_jp = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(blank=True, null=True)
    dissapeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
