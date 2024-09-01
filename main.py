from fastapi import FastAPI, Body
from datetime import datetime
#from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import List, Optional

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

# Validación de tipops de datos
class Pokemon(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=50, default="Pokemon")
    type : str = Field(max_length=15, default="Normal")
    abilities : list = Field(min_length=1, default=["tacle"])
    base_stats : dict

@app.delete('/pokemons/delete/{id}', tags=['pokemons'])
def delete_pokemon(id: int):
    """
    Elimina un Pokémon de la base de datos en función de su ID.

    Args:
        id (int): El ID del Pokémon a eliminar.

    Returns:
        list: La lista actualizada de Pokémon después de la eliminación.
    """
    for poke in pokemon_data:
        if poke['id'] == id:
            pokemon_data.remove(poke)
    return pokemon_data


# Need to fix that
@app.put('/pokemons/update/{id}', tags=['pokemons'])
def update_pokemon(id: int, pokemon: Pokemon):
    """
    Actualiza la información de un Pokémon en la base de datos.

    Args:
        id (int): El ID del Pokémon a actualizar.
        name (str): El nuevo nombre del Pokémon.
        type (str): El nuevo tipo del Pokémon.
        abilities (list): La nueva lista de habilidades del Pokémon.
        base_stats (dict): El nuevo conjunto de estadísticas base del Pokémon.

    Returns:
        list: La lista actualizada de Pokémon después de la modificación.
    """
    for poke in pokemon_data:
        if poke['id'] == id:
            poke['name'] = pokemon.name
            poke['type'] = pokemon.type
            poke['abilities'] = pokemon.abilities
            poke['base_stats'] = pokemon.base_stats
            return pokemon_data

    # Si no se encuentra el Pokémon con el ID dado, se podría manejar el caso aquí:
    return {"error": "Pokémon no encontrado"}
            

@app.post('/pokemons/create', tags=['pokemons'])
def create_pokemon(pokemon: Pokemon):
    """
    Crea un nuevo Pokémon y lo agrega a la base de datos.

    Args:
        id (int): El ID del nuevo Pokémon.
        name (str): El nombre del nuevo Pokémon.
        type (str): El tipo del nuevo Pokémon.
        abilities (list): La lista de habilidades del nuevo Pokémon.
        base_stats (dict): El conjunto de estadísticas base del nuevo Pokémon.

    Returns:
        list: La lista actualizada de Pokémon después de la creación.
    """
    pokemon_data.append(pokemon)
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


###################################### EXERCISE 1 #######################################
# Fake Data
dishes = [
    {
        "id": 1,
        "name": "Alfredo Pasta",
        "price": 12.99,
        "desc": "Al dente pasta with creamy Alfredo sauce, Parmesan cheese, and chicken pieces."
    },
    {
        "id": 2,
        "name": "Carnitas Tacos",
        "price": 9.50,
        "desc": "Corn tortillas filled with pork carnitas, onion, cilantro, and green salsa."
    },
    {
        "id": 3,
        "name": "Tuna Sushi Roll",
        "price": 14.00,
        "desc": "Sushi roll filled with fresh tuna, avocado, and cucumber, served with soy sauce."
    },
    {
        "id": 4,
        "name": "Margherita Pizza",
        "price": 11.75,
        "desc": "Classic pizza with tomato sauce, fresh mozzarella, and basil."
    },
    {
        "id": 5,
        "name": "Caesar Salad",
        "price": 8.25,
        "desc": "Crisp romaine lettuce, croutons, Parmesan cheese, and homemade Caesar dressing."
    }
]


@app.get('/exercise-1', tags=['ejercicio 1'])
def get_dishes():
    return [dish for dish in dishes]


@app.get('/exercise-1/{id}', tags=['ejercicio 1'])
def get_dish(id: int):
    return [dish for dish in dishes if dish['id'] == id]

###################################### EXERCISE 2 #######################################

# Fake Data

patients_data = [
    {
        "id": 1,
        "name": "John",
        "last_name": "Doe",
        "birthdate": "2015-04-12"
    },
    {
        "id": 2,
        "name": "Emily",
        "last_name": "Smith",
        "birthdate": "1990-07-23"
    },
    {
        "id": 3,
        "name": "Michael",
        "last_name": "Johnson",
        "birthdate": "1978-11-30"
    },
    {
        "id": 4,
        "name": "Sophia",
        "last_name": "Williams",
        "birthdate": "2002-03-15"
    },
    {
        "id": 5,
        "name": "David",
        "last_name": "Brown",
        "birthdate": "2010-09-05"
    }
]


def is_minor(birthdate: str):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthdate.year
    return age < 18


@app.get('/exercise-2', tags=['ejercicio 2'])
def get_patients():
    return [patient for patient in patients_data]


@app.get('/exercise-2/minors', tags=['ejercicio 2'])
def get_minors_patients():
    return [patient for patient in patients_data if(is_minor(patient['birthdate']))]




###################################### EXERCISE 3 DTO #######################################
# Definición de los modelos de datos
class Patient(BaseModel):
    id: int
    name: str
    last_name: str
    birthdate: str

class Hospital(BaseModel):
    id: int
    hospital: str

class TurnDTO(BaseModel):
    id: int
    paciente: str
    hospital_name: str

hospital = [{"id": 1, "hospital": "Garraham"}]

@app.get("/turno", response_model=List[TurnDTO])
def get_turno():
    turnos = []
    for patient in patients_data:
        hospital_data = next((h for h in hospital if h["id"] == patient["id"]), None)
        if hospital_data:
            turno = TurnDTO(
                id=patient["id"],
                paciente=patient["name"],
                hospital_name=hospital_data["hospital"]
            )
            turnos.append(turno)
    return turnos