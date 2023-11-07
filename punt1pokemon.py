# Datos de los Pokémon (ejemplo)
pokemons = [
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
    # ... otros Pokémon ...
]

# Construir árboles con índices para nombre, número y tipo
pokemon_por_nombre = {}
pokemon_por_numero = {}
pokemon_por_tipo = {}

for pokemon in pokemons:
    # Índice por nombre
    nombre = pokemon["nombre"]
    if nombre not in pokemon_por_nombre:
        pokemon_por_nombre[nombre] = pokemon

    # Índice por número
    numero = pokemon["numero"]
    if numero not in pokemon_por_numero:
        pokemon_por_numero[numero] = pokemon

    # Índice por tipo
    tipos = pokemon["tipo"]
    for tipo in tipos:
        if tipo in pokemon_por_tipo:
            pokemon_por_tipo[tipo].append(pokemon)
        else:
            pokemon_por_tipo[tipo] = [pokemon]

# Acceder a los datos de un Pokémon de manera eficiente
nombre_buscado = "Pikachu"
numero_buscado = 25
tipo_buscado = "Eléctrico"

pokemon_por_nombre_encontrado = pokemon_por_nombre.get(nombre_buscado)
pokemon_por_numero_encontrado = pokemon_por_numero.get(numero_buscado)
pokemon_por_tipo_encontrado = pokemon_por_tipo.get(tipo_buscado)

if pokemon_por_nombre_encontrado:
    print("Pokémon encontrado por nombre:", pokemon_por_nombre_encontrado)

if pokemon_por_numero_encontrado:
    print("Pokémon encontrado por número:", pokemon_por_numero_encontrado)

if pokemon_por_tipo_encontrado:
    print("Pokémon(s) encontrado(s) por tipo:", pokemon_por_tipo_encontrado)
    
def buscar_pokemon_por_numero(numero):
    return pokemon_por_numero.get(numero)

# Función para buscar Pokémon por nombre o proximidad en el nombre
def buscar_pokemon_por_nombre(nombre):
    resultados = []
    for pokemon_nombre, pokemon_info in pokemon_por_nombre.items():
        if nombre.lower() in pokemon_nombre.lower():
            resultados.append(pokemon_info)
    return resultados

# Búsqueda por número
numero_buscado = 25
pokemon_por_numero_encontrado = buscar_pokemon_por_numero(numero_buscado)

if pokemon_por_numero_encontrado:
    print("Pokémon encontrado por número:", pokemon_por_numero_encontrado)
else:
    print("Pokémon con número", numero_buscado, "no encontrado.")

# Búsqueda por nombre o proximidad
nombre_buscado = "bul"
pokemones_por_nombre_encontrados = buscar_pokemon_por_nombre(nombre_buscado)

if pokemones_por_nombre_encontrados:
    print("Pokémon(s) encontrados por nombre o proximidad:")
    for pokemon in pokemones_por_nombre_encontrados:
        print(pokemon)
else:
    print("Ningún Pokémon encontrado con nombre o proximidad a", nombre_buscado)

tipo_buscado = "Agua"

# Tipos de Pokémon que deseas buscar
tipos_buscados = ["Agua", "Fuego", "Planta", "Eléctrico"]

# Mostrar nombres de Pokémon para cada tipo
for tipo in tipos_buscados:
    pokemones_de_tipo = pokemon_por_tipo.get(tipo, [])
    if pokemones_de_tipo:
        print("Pokémon(s) de tipo", tipo + ":")
        for pokemon in pokemones_de_tipo:
            print(pokemon["nombre"])
    else:
        print("No se encontraron Pokémon de tipo", tipo)

