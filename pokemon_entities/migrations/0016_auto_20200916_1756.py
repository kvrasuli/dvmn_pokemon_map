# Generated by Django 2.2.3 on 2020-09-16 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20200916_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entities', to='pokemon_entities.Pokemon', verbose_name='Название покемона'),
        ),
    ]