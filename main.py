from fastapi import FastAPI, Body
#from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'mi app con fastAPI'
app.version = '1.0'

pokemon_data = [
    {
        "id": 1,
        "name": "Pikachu",
        "type": "Electric",
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
        "id": 2,
        "name": "Charmander",
        "type": "Fire",
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
        "id": 3,
        "name": "Bulbasaur",
        "type": "Poison",
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
        "id": 4,
        "name": "Squirtle",
        "type": "Water",
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
        "id": 5,
        "name": "Eevee",
        "type": "Normal",
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




@app.delete('/pokemons/delete/{id}',tags=['pokemons'])
def delete_pokemon(id: int):
    for poke in pokemon_data:
        if poke['id'] == id:
            pokemon_data.remove(poke)
    return pokemon_data


@app.put('/pokemons/update/')
def update_pokemon(id: int = Body(), 
                   name: str = Body(), 
                   type: str = Body(), 
                   abilities: list = Body(), 
                   base_stats: dict = Body()):
    
    for poke in pokemon_data:
        if poke['id'] == id:
            poke['name'] = name
            poke['type'] = type
            poke['abilities'] = abilities
            poke['base_stats'] = base_stats

            return pokemon_data
            

@app.post('/pokemons/create', tags=['pokemons'])
def create_pokemon(id: int = Body(), 
                   name: str = Body(), 
                   type: str = Body(), 
                   abilities: list = Body(), 
                   base_stats: dict = Body()):
    
    pokemon_data.append({
        "id": id,
        "name": name,
        "type": type,
        "abilities": abilities,
        "base_stats": base_stats
    })

    return pokemon_data


@app.get('/', tags=['inicio'])
def message():
    """
    GET /

    **Descripción:**
    Este endpoint devuelve un mensaje de saludo.

    **Respuesta:**
    - 200 OK: Devuelve el mensaje "hola mundo".
    """
    return 'hola mundo'


@app.get('/pokemons', tags=['pokemons'])
def get_pokemons():
    """
    GET /pokemons

    **Descripción:**
    Este endpoint devuelve la lista completa de Pokémon.

    **Respuesta:**
    - 200 OK: Devuelve una lista de objetos JSON que representan a todos los Pokémon.
    """
    return pokemon_data


@app.get('/pokemons/{id}', tags=['pokemons'])
def get_pokemon_by_id(id: int):
    """
    GET /pokemons/{id}

    **Descripción:**
    Este endpoint devuelve la información de un Pokémon específico basado en su `id`.

    **Parámetros:**
    - `id` (int): El identificador único del Pokémon.

    **Respuesta:**
    - 200 OK: Devuelve un objeto JSON con los datos del Pokémon si se encuentra.
    - 404 Not Found: Devuelve una lista vacía si no se encuentra el Pokémon con el `id` proporcionado.
    """
    return [pokemon for pokemon in pokemon_data if pokemon['id'] == id]


@app.get('/pokemons/', tags=['pokemons'])
def get_pokemons_by_type(poke_type: str):
    """
    GET /pokemons/

    **Descripción:**
    Este endpoint devuelve una lista de Pokémon que coinciden con el tipo especificado.

    **Parámetros:**
    - `poke_type` (str): El tipo de Pokémon a filtrar (por ejemplo, "Fire", "Water").

    **Respuesta:**
    - 200 OK: Devuelve una lista de Pokémon que tienen el tipo especificado.
    """
    return [ pokemon for pokemon in pokemon_data if pokemon['type'] == poke_type] 


