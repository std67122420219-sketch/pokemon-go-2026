pokemon_types = [
  'Water','Fire','Grass','Electric','Psychic','Dragon',
  'Dark','Fairy','Normal','Fighting','Flying','Poison',
  'Ground','Rock','Bug','Ghost','Steel','Ice'
]

from pokemon.models import Type
types = [Type(name=type) for type in pokemon_types]