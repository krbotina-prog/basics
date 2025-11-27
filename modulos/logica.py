import os
# Importamos los datos
from modulos import datos

def limpiar_pantalla():
    """Borra todo el texto de la consola para dibujar de nuevo"""
    # Si estás en Windows usa 'cls', si es Mac/Linux usa 'clear'
    # Como vi que usas Windows en la foto, dejamos 'cls'
    os.system('cls')

def mostrar_juego():
    """Imprime el mapa carácter por carácter"""
    limpiar_pantalla()
    print(f"PUNTAJE: {datos.puntaje}")
    print("Usa W (arriba), S (abajo), A (izquierda), D (derecha) y ENTER")
    print("-" * 20)

    # Recorremos el mapa para imprimirlo
    for f in range(len(datos.mapa)):
        fila_texto = ""
        for c in range(len(datos.mapa[f])):
            # Si esta es la posición de pacman, dibujamos la P
            if f == datos.pacman_fila and c == datos.pacman_col:
                fila_texto = fila_texto + "O"  # Usamos 'O' para Pacman
            else:
                # Si no es pacman, dibujamos lo que haya en el mapa (# o .)
                fila_texto = fila_texto + datos.mapa[f][c]
        print(fila_texto)

def procesar_movimiento(tecla):
    """Calcula la nueva posición basado en la tecla"""
    # Copiamos la posición actual a variables temporales
    nueva_fila = datos.pacman_fila
    nueva_col = datos.pacman_col

    # Definimos los cambios según la tecla (WASD)
    if tecla == 'w':
        nueva_fila = nueva_fila - 1
    elif tecla == 's':
        nueva_fila = nueva_fila + 1
    elif tecla == 'a':
        nueva_col = nueva_col - 1
    elif tecla == 'd':
        nueva_col = nueva_col + 1
    
    # VERIFICAR COLISIÓN (Programación estructural pura)
    # Miramos qué hay en la casilla a la que queremos ir
    contenido_destino = datos.mapa[nueva_fila][nueva_col]

    if contenido_destino != '#':  # Si NO es pared
        # Actualizamos la posición real
        datos.pacman_fila = nueva_fila
        datos.pacman_col = nueva_col

        # Si había comida, sumamos puntos y borramos la comida
        if contenido_destino == '.':
            datos.puntaje = datos.puntaje + 10
            datos.mapa[nueva_fila][nueva_col] = ' ' # Dejamos vacío
            