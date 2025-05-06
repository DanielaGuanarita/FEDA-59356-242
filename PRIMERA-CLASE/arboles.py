class Nodo:
    def __init__(self, pregunta, izquierda=None, derecha=None):
        self.pregunta = pregunta
        self.izquierda = izquierda
        self.derecha = derecha

raiz = Nodo('Es una señal periodica?',
            Nodo('Tiene variaciones de intensidad?',
                Nodo('Señal modulada'),
                Nodo('Señno
                al recurrente')),
            Nodo('Es un patron reconocible?',
                Nodo('Señal codificada'),
                Nodo('Señal desconocida')))

def clasificar_senal(nodo):
    if nodo.izquierda is None and nodo.derecha is None:
        return(f'Clasificación: {nodo.pregunta}')
    respuesta = input(nodo.pregunta + '(si/no):').lower()
    if respuesta == 'si':
        return clasificar_senal(nodo.izquierda)
    else:
        return clasificar_senal(nodo.derecha)

print(clasificar_senal(raiz))

