#Autor: Joshua Sánchez Martínez A01274269
#Cumple con una serie de funciones con distintos fines


#Recibe como parametros una lista de numeros enteros y regresa una nueva lista con solo valores pares
def extraerPares(lista):
    lN = lista[:]
    for n in lista:
        if n%2 != 0:
            lN.remove(n)

    return lN


#Recibe como parametros una lista de numeros enteros y regresa una nueva lista con los valores que son mayores al previo
def extraerMayoresPrevio(lista):
    lN = []
    for n in range(1, len(lista)-1):
        if lista[n] > lista[n-1]:
            lN.append(lista[n])
    return lN


#Recibe como parametros una lista de numeros enteros y regresa una nueva lista con cada opareja de datos intercambiada
def intercambiarParejas(lista):
    lN = []
    n = len(lista)
    if n == 0:
        return lN
    if n % 2 != 0:
        for d in range(0, n - 1, 2):
            lN.append(lista[d + 1])
            lN.append(lista[d])
        lN.append(lista[-1])
        return lN
    if n % 2 == 0:
        for d in range(0, n, 2):
            lN.append(lista[d + 1])
            lN.append(lista[d])
        return lN


#Recibe como parametros una lista de numeros enteros e intercambia el mayor y el menor
def intercambiarMM(lista):
    me = lista[0]
    ma = lista[len(lista)-1]
    lista[len(lista)-1] = me
    lista[0] = ma
    return lista


#Recibe como parametros una lista de numeros enteros y regresa el promedio sin tomar en cuenta el mayor y el menor valor
def promediarCentro(lista):
    lN = lista[:]
    p = 0
    if len(lista) > 0:
        lN.remove(min(lista))
        lN.remove(max(lista))
        if len(lN) != 0:
            p = int(sum(lN)/len(lN))

    return p


#Recibe como parametros una lista de numeros enteros y regresa una dupla con la media y la desviación estandar
def calcularEstadistica(lista):
    a = 0
    for n in range(0, len(lista) - 1):
        a += lista[n]
    media = a / len(lista)
    for n in range(0, len(lista) - 1):
        a += lista[n]-media
    a = a**2
    a = a / (len(lista)-1)
    desviacion = a**.5
    return media, desviacion


#Recibe como parametros una lista de numeros enteros y regresa una suma sin tomar el 13 y los que lo rodean
def calcularSuma(lista):
    n = len(lista)
    suma = 0
    if n == 0:
        return suma
    if n == 1:
        suma += lista[0]
        return suma
    if lista[0] != 13:
        suma += lista[0]
    for v in range(1, n - 1):
        if lista[v] != 13 and lista[v + 1] != 13 and (lista[v - 1]) != 13:
            suma += lista[v]
        if lista[0] and lista[1] != 13:
            suma += lista[0]
        if lista[-1] and lista[-2] != 13:
            suma += lista[1]
    return suma


#Funcion principal
def main():
    lista = [1,2,3,2,4,13,14,60,5,8,3,22,44,55]
    print(extraerPares(lista))
    print(extraerMayoresPrevio(lista))
    print(intercambiarParejas(lista))
    print(intercambiarMM(lista))
    print(promediarCentro(lista))
    print(calcularEstadistica(lista))
    print(calcularSuma(lista))


#lLama a la funcion principal
main()
