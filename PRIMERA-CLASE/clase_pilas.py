# class Pila:
#     def __init__(self):
#         self.elementos = []
    
#     def apilar(self, elemento):
#         self.elementos.append(elemento)

#     def desapilar(self):
#         if not self.esta_vacia():
#             return self.elementos.pop()
#         else:
#             return 'La lista esta vacía.'

#     def esta_vacia(self):
#         return len(self.elementos)== 0

#     def ver_tope(self):
#         if not self.esta_vacia():
#             return self.elementos[-1]
#         else:
#             return 'La pila esta vacía.'

# mi_pila = Pila()
# mi_pila.apilar(3)
# mi_pila.apilar(4)
# mi_pila.apilar(5)
# print('Elemento en el tope: ', mi_pila.ver_tope())
# print('Esta vacia: ', mi_pila.esta_vacia())
# print('Elemento eliminado: ', mi_pila.desapilar())
# print('Elemento eliminado: ', mi_pila.desapilar())
# print('Elemento eliminado: ', mi_pila.desapilar())
# print('Esta vacia: ', mi_pila.esta_vacia())



#estacion de control

class Torre_de_control:
    def __init__(self):
        self.naves = []
    
    def entrada_naves(self, nave):
        self.naves.append(nave)

    def salida_naves(self):
        if not self.sin_naves():
            return self.naves.pop()
        else:
            return 'No hay naves en plataforma.'

    def sin_naves(self):
        return len(self.naves)== 0

    def ver_salida_naves(self):
        if not self.sin_naves():
            return self.naves[-1]
        else:
            return 'No hay naves en plataforma.'

pista_despegue = Torre_de_control()
pista_despegue.entrada_naves('Apolo')
pista_despegue.entrada_naves('Discovery')
pista_despegue.entrada_naves('Orión')

print('Nave por despegar: ', pista_despegue.ver_salida_naves())
print('Esta vacia la pista: ', pista_despegue.sin_naves())
print('Nave que despego: ', pista_despegue.salida_naves())
print('Nave que despego: ', pista_despegue.salida_naves())
print('Nave que despego: ', pista_despegue.salida_naves())
print('Esta vacia la pista: ', pista_despegue.sin_naves())
