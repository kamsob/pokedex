from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'description', 'image', 'move1', 'move2', 'move3', 'move4']