from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'description', 'image', 'move1', 'move2', 'move3', 'move4']
