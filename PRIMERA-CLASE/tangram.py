class Pieza:
    def __init__(self, nombre, tamaño, x=0, y=0, rotacion=0):
        self.nombre = nombre
        self.tamaño = tamaño
        self.posicion = (x, y)
        self.rotacion = rotacion

    def rotar(self, grados):
        self.rotacion = (self.rotacion + grados) % 360
        return f"{self.nombre} rotado {grados}° (Total: {self.rotacion}°)"

    def mover(self, x, y):
        self.posicion = (x, y)
        return f"{self.nombre} movido a la posición {self.posicion}"

    def obtener_instruccion(self):
        return f"Coloca {self.nombre} en {self.posicion} con rotación {self.rotacion}°"

# Piezas estándar del Tangram
def crear_piezas():
    return [
        Pieza("Triángulo grande 1", "grande"),
        Pieza("Triángulo grande 2", "grande"),
        Pieza("Triángulo mediano", "mediano"),
        Pieza("Triángulo pequeño 1", "pequeño"),
        Pieza("Triángulo pequeño 2", "pequeño"),
        Pieza("Cuadrado", "cuadrado"),
        Pieza("Paralelogramo", "paralelogramo"),
    ]

# Instrucciones para la figura del Cohete
def figura_cohete():
    piezas = crear_piezas()
    instrucciones = []

    instrucciones.append(piezas[0].mover(1, 3))  # Triángulo grande 1
    instrucciones.append(piezas[0].rotar(45))
    
    instrucciones.append(piezas[1].mover(3, 3))  # Triángulo grande 2
    instrucciones.append(piezas[1].rotar(135))
    
    instrucciones.append(piezas[2].mover(2, 1))  # Triángulo mediano
    instrucciones.append(piezas[2].rotar(0))
    
    instrucciones.append(piezas[3].mover(1, 1))  # Triángulo pequeño 1
    instrucciones.append(piezas[3].rotar(0))
    
    instrucciones.append(piezas[4].mover(3, 1))  # Triángulo pequeño 2
    instrucciones.append(piezas[4].rotar(0))
    
    instrucciones.append(piezas[5].mover(2, 2))  # Cuadrado
    instrucciones.append(piezas[5].rotar(45))
    
    instrucciones.append(piezas[6].mover(0, 2))  # Paralelogramo
    instrucciones.append(piezas[6].rotar(270))
    
    return [pieza.obtener_instruccion() for pieza in piezas]

# Instrucciones para la figura de la T
def figura_t():
    piezas = crear_piezas()
    instrucciones = []

    instrucciones.append(piezas[0].mover(0, 3))  # Triángulo grande 1
    instrucciones.append(piezas[0].rotar(0))

    instrucciones.append(piezas[1].mover(2, 3))  # Triángulo grande 2
    instrucciones.append(piezas[1].rotar(0))

    instrucciones.append(piezas[2].mover(1, 0))  # Triángulo mediano
    instrucciones.append(piezas[2].rotar(180))

    instrucciones.append(piezas[3].mover(1, 1))  # Triángulo pequeño 1
    instrucciones.append(piezas[3].rotar(90))

    instrucciones.append(piezas[4].mover(1, 2))  # Triángulo pequeño 2
    instrucciones.append(piezas[4].rotar(90))

    instrucciones.append(piezas[5].mover(1, 3))  # Cuadrado
    instrucciones.append(piezas[5].rotar(0))

    instrucciones.append(piezas[6].mover(1, 4))  # Paralelogramo
    instrucciones.append(piezas[6].rotar(90))

    return [pieza.obtener_instruccion() for pieza in piezas]

# Menú para el jugador
def menu():
    while True:
        print("\n--- Tangram - Ayuda para construir figuras ---")
        print("1. Construir figura: Cohete")
        print("2. Construir figura: T")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nInstrucciones para construir el Cohete:")
            for instruccion in figura_cohete():
                print("🔹", instruccion)
        elif opcion == "2":
            print("\nInstrucciones para construir la figura T:")
            for instruccion in figura_t():
                print("🔹", instruccion)
        elif opcion == "3":
            print("¡Gracias por jugar al Tangram!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

