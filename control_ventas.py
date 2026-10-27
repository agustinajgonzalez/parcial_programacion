def calcular_total(ventas):
    total = 0

    for i in range(len(ventas)):
        total += ventas[i]

    return total


def calcular_promedio(ventas):
    if len(ventas) == 0:
        return 0

    return calcular_total(ventas) / len(ventas)


def calcular_porcentaje(venta, total):
    if total == 0:
        return 0

    return venta * 100 / total


def buscar_menor(ventas):
    if len(ventas) == 0:
        return None

    menor = ventas[0]

    for i in range(1, len(ventas)):
        if ventas[i] < menor:
            menor = ventas[i]

    return menor


def buscar_mayor(ventas):
    if len(ventas) == 0:
        return None

    mayor = ventas[0]

    for i in range(1, len(ventas)):
        if ventas[i] > mayor:
            mayor = ventas[i]

    return mayor