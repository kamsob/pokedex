from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from .forms import PokemonForm
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

@parser_classes((MultiPartParser, FormParser))
def pokemon_list(request, format=None):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        
        # HTML
        if 'text/html' in request.META.get('HTTP_ACCEPT', ''):
            return render(request, 'pokedex.html', {'pokemons': pokemons})
        
        # JSON
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)

def upload_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex')
    else:
        form = PokemonForm()
    return render(request, 'upload_pokemon.html', {'form': form})

@api_view(['GET', 'PUT'])
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'edit_pokemon.html', {'form': form, 'pokemon': pokemon})