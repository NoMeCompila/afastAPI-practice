from fastapi import FastAPI
#from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'mi app con fastAPI'
app.version = '1.0'

pokemon_data = [
    {
        "name": "Pikachu",
        "type": ["Electric"],
        "abilities": ["Static", "Lightning Rod"],
        "base_stats": {
            "hp": 35,
            "attack": 55,
            "defense": 40,
            "special_attack": 50,
            "special_defense": 50,
            "speed": 90
        }
    },
    {
        "name": "Charmander",
        "type": ["Fire"],
        "abilities": ["Blaze", "Solar Power"],
        "base_stats": {
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "special_attack": 60,
            "special_defense": 50,
            "speed": 65
        }
    },
    {
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "abilities": ["Overgrow", "Chlorophyll"],
        "base_stats": {
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "special_attack": 65,
            "special_defense": 65,
            "speed": 45
        }
    },
    {
        "name": "Squirtle",
        "type": ["Water"],
        "abilities": ["Torrent", "Rain Dish"],
        "base_stats": {
            "hp": 44,
            "attack": 48,
            "defense": 65,
            "special_attack": 50,
            "special_defense": 64,
            "speed": 43
        }
    },
    {
        "name": "Eevee",
        "type": ["Normal"],
        "abilities": ["Run Away", "Adaptability", "Anticipation"],
        "base_stats": {
            "hp": 55,
            "attack": 55,
            "defense": 50,
            "special_attack": 45,
            "special_defense": 65,
            "speed": 55
        }
    }
]


@app.get('/', tags=['inicio'])
def message():
    return 'hola mundo'


@app.get('/pokemons', tags=['pokemons'])
def get_pokemons():
    return pokemon_data