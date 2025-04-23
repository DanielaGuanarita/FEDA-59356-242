import random

# Clase Nave
class Nave:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre}, prioridad: {self.prioridad}"

    def prioridad_valor(self):
        prioridades = {"Alta": 3, "Media": 2, "Baja": 1}
        return prioridades[self.prioridad]

# Clase Generador de Naves
class GeneradorDeNaves:
    def __init__(self):
        self.nombres_posibles = [
            "Apolo", "Discovery", "Orión", "Endeavour", "Atlantis",
            "Challenger", "Columbia", "Soyuz", "Dragon", "Starship"
        ]
        self.prioridades_posibles = ["Alta", "Media", "Baja"]

    def generar_naves(self, cantidad=10):
        naves = []
        nombres = random.sample(self.nombres_posibles, cantidad)
        for nombre in nombres:
            prioridad = random.choice(self.prioridades_posibles)
            naves.append(Nave(nombre, prioridad))
        return naves

# Clase Torre de Control con manejo de prioridades y LIFO
class TorreDeControl:
    def __init__(self):
        # Usamos una pila para cada prioridad
        self.pilas = {
            "Alta": [],
            "Media": [],
            "Baja": []
        }

    def aterrizar_naves(self, naves):
        random.shuffle(naves)
        print("\n*Naves aterrizando en la plataforma*")
        for nave in naves:
            print(f"La nave '{nave.nombre}' con prioridad '{nave.prioridad}' ha aterrizado.")
            self.pilas[nave.prioridad].append(nave)

    def mostrar_naves(self):
        print("\n*Naves en la plataforma por prioridad*")
        for prioridad in ["Alta", "Media", "Baja"]:
            print(f"\nPrioridad {prioridad}:")
            if not self.pilas[prioridad]:
                print("  - Ninguna nave.")
            else:
                for nave in reversed(self.pilas[prioridad]):
                    print(f"  - {nave.nombre}")

    def despegar_naves(self):
        print("\n*Naves despegando según prioridad y orden de llegada*")
        for prioridad in ["Alta", "Media", "Baja"]:
            while self.pilas[prioridad]:
                nave = self.pilas[prioridad].pop()
                print(f"La nave '{nave.nombre}' con prioridad '{nave.prioridad}' ha despegado.")

    def plataforma_vacia(self):
        return all(len(pila) == 0 for pila in self.pilas.values())

# Función principal
if __name__ == "__main__":
    generador = GeneradorDeNaves()
    naves = generador.generar_naves()

    torre = TorreDeControl()
    torre.aterrizar_naves(naves)
    torre.mostrar_naves()

    torre.despegar_naves()

    if torre.plataforma_vacia():
        print("\nTodas las naves han despegado. Plataforma vacía.")
