import random


def baraja_francesa():
    palos = ["♠", "♥", "♦", "♣"]
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As"]
    
    baraja = [[f"{valor}{palo}" for valor in valores] for palo in palos]
    return baraja, valores, palos


baraja, valores, palos = baraja_francesa()

print("Baraja francesa:")
for palo, cartas in zip(palos, baraja):
    print(f"{', '.join(cartas)}")



palo1_idx, valor1_idx = random.randint(0, 3), random.randint(0, 12)
palo2_idx, valor2_idx = random.randint(0, 3), random.randint(0, 12)

carta1 = baraja[palo1_idx][valor1_idx]
carta2 = baraja[palo2_idx][valor2_idx]



print(f"\nHas sacado: {carta1}")
print(f"Has sacado: {carta2}")


valor_carta1 = "".join(filter(str.isdigit, carta1)) or carta1[:-1]
valor_carta2 = "".join(filter(str.isdigit, carta2)) or carta2[:-1]


orden_valores = {valor: i for i, valor in enumerate(valores)}
orden_palos = {palo: i for i, palo in enumerate(palos)}


if orden_valores.get(valor_carta1, -1) > orden_valores.get(valor_carta2, -1):
    resultado = carta1
elif orden_valores.get(valor_carta1, -1) < orden_valores.get(valor_carta2, -1):
    resultado = carta2
else:
    
    if orden_palos[palo_carta1] > orden_palos[palo_carta2]:
        resultado = carta1
    elif orden_palos[palo_carta1] < orden_palos[palo_carta2]:
        resultado = carta2
    else:
        resultado = "Son iguales"

print(f"\nLa carta mayor es: {resultado}")
