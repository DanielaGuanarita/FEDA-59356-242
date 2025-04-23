import random
from collections import deque

class GeneradorDeMensajes:
    def __init__(self):
        self.mensajes_posibles = [
            "Saludo: ¡Saludos desde el planeta Xeno!",
            "Mensaje de alerta: asteroide peligroso en curso.",
            "Intercambio cultural: recetas interestelares.",
            "Código desconocido detectado: 10111010.",
            "Transmisión perdida: reintentar conexión.",
            "Solicitud de alianza intergaláctica: coordenadas incluidas.",
            "Advertencia: anomalía espacial detectada cerca de tu estación.",
            "Reporte científico: nueva forma de vida descubierta en el sector Z-21.",
            "Saludo: Saludos cordiales de la Federación de Pléyades.",
            "Mensaje codificado: tecnología avanzada para intercambio."
        ]

    def generar_mensaje(self):
        return random.choice(self.mensajes_posibles)

class ColaMensaje:
    def __init__(self):
        self.cola = deque()

    def agregar_mensajes_aleatorios(self, generador, cantidad=5):
        for _ in range(cantidad):
            mensaje = generador.generar_mensaje()
            self.cola.append(mensaje)

    def procesar_mensajes_prioritarios(self):
        if not self.cola:
            print("La cola está vacía. No hay mensajes para procesar.")
            return

        print("Procesando mensajes (saludos al final):")
        no_saludos = deque()
        saludos = deque()

        # Separar los mensajes según tipo
        while self.cola:
            mensaje = self.cola.popleft()
            if "Saludo" in mensaje:
                saludos.append(mensaje)
            else:
                no_saludos.append(mensaje)

        # Procesar primero no saludos
        for mensaje in no_saludos:
            print(f"Procesando mensaje: {mensaje}")

        # Luego procesar los saludos
        for mensaje in saludos:
            print(f"Procesando saludo: {mensaje}")

    def mostrar_primer_mensaje(self):
        if self.cola:
            print(f"Mensaje más antiguo en la cola: {self.cola[0]}")
        else:
            print("La cola está vacía. No hay mensajes para mostrar.")

    def verificar_si_vacia(self):
        if not self.cola:
            print("La cola de mensajes está vacía.")
        else:
            print("La cola de mensajes NO está vacía.")

    def mostrar_cola(self):
        if not self.cola:
            print("La cola está vacía.")
        else:
            print("Mensajes en la cola:")
            for i, mensaje in enumerate(self.cola, 1):
                print(f"{i}. {mensaje}")

# --- Simulación ---
generador = GeneradorDeMensajes()
cola = ColaMensaje()

print("1. Agregando 5 mensajes aleatorios a la cola:")
cola.agregar_mensajes_aleatorios(generador)
cola.mostrar_cola()
print("-" * 40)

print("2. Mostrando el mensaje más antiguo sin procesarlo:")
cola.mostrar_primer_mensaje()
print("-" * 40)

print("3. Verificando si la cola está vacía:")
cola.verificar_si_vacia()
print("-" * 40)

print("4. Procesando mensajes (saludos al final):")
cola.procesar_mensajes_prioritarios()
print("-" * 40)

print("5. Cola final tras procesar (debe estar vacía):")
cola.verificar_si_vacia()

