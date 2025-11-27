# Variables del Jugador
pacman_fila = 1  # Posición vertical inicial (Y)
pacman_col = 1   # Posición horizontal inicial (X)
puntaje = 0

# El Mapa: 
# # = Pared
# . = Comida
#   = Espacio vacío
# P = Pacman (lo dibujaremos dinámicamente)
mapa_original = [
    "####################",
    "#..................#",
    "#.##.###.##.###.##.#",
    "#.##.###.##.###.##.#",
    "#..................#",
    "#.##.#.######.#.##.#",
    "#....#...##...#....#",
    "####.### ## ###.####",
    "####.#        #.####",
    "####.# ###### #.####",
    "#..................#",
    "####################"
]

# Convertimos el mapa en una lista de listas (matriz) editable
mapa = []
for linea in mapa_original:
    mapa.append(list(linea))