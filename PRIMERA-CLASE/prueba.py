#utilizamos random.sample  
# para crear 10 naves diferentes y queremos que el orden sea aleatorio 
# cada vez que se pruebe sin hacer la comprobacion manual a diferencia de los otros 
# metodos que permiten repetir nombres o que no nos muestran la lista original 

#utilizamos key=lambda para organizar la lista por valor prioridad 
#y que asi vaya al inicio de la lista 


import random


class Nave:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad  

    def __str__(self):
        return f"{self.nombre}, prioridad: {self.prioridad}"

    def valor_prioridad(self):
        prioridades = {"Alta": 3, "Media": 2, "Baja": 1}
        return prioridades[self.prioridad]


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


class TorreDeControl:
    def __init__(self):
        self.pila = []

    def aterrizar_naves(self, naves):
        print("\n **Naves aterrizando en la plataforma**")
        for nave in naves:
            print(f"La nave '{nave.nombre}' con prioridad '{nave.prioridad}' ha aterrizado.")
            self.pila.append(nave)

    def mostrar_naves(self):
        if not self.pila:
            print("La plataforma está vacía.")
            return
        print("\n **Naves en la plataforma**")
        for nave in reversed(self.pila):
            print(f"Nave: {nave.nombre}, prioridad: {nave.prioridad}")

    def despegar_naves(self):
        print("\n **Despegue de naves por prioridad**")
        prioridades = {"Alta": 3, "Media": 2, "Baja": 1}
        while self.pila:
            # Buscar nave con prioridad más alta
            mayor_prioridad = max(nave.valor_prioridad() for nave in self.pila)
            for i in range(len(self.pila)-1, -1, -1):  # Recorrer desde el tope de la pila
                if self.pila[i].valor_prioridad() == mayor_prioridad:
                    nave = self.pila.pop(i)
                    print(f"La nave '{nave.nombre}' con prioridad '{nave.prioridad}' ha despegado.")
                    break

    def plataforma_vacia(self):
        return len(self.pila) == 0


if __name__ == "__main__":
    generador = GeneradorDeNaves()
    naves = generador.generar_naves()

    torre = TorreDeControl()
    torre.aterrizar_naves(naves)
    torre.mostrar_naves()

    torre.despegar_naves()

    if torre.plataforma_vacia():
        print("\nTodas las naves han despegado. Plataforma vacía.")
