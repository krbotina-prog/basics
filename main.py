from modulos import logica

# Bucle infinito del juego
juego_activo = True

while juego_activo:
    # 1. Mostrar el mapa actual
    logica.mostrar_juego()

    # 2. Pedir al usuario qué hacer
    # lower() convierte lo que escribas a minúscula para que no importe si usas Mayúsculas
    direccion = input("Tu movimiento: ").lower()

    # 3. Opción para salir
    if direccion == 'salir':
        juego_activo = False
        print("¡Juego terminado!")
    else:
        # 4. Mover al personaje
        logica.procesar_movimiento(direccion)