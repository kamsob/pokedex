# Generated by Django 5.1.5 on 2025-01-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_moves_alter_pokemon_name_pokemon_moves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='moves',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='move4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Moves',
        ),
    ]
