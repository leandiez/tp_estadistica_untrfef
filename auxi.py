import math

#Funciones auxiliares

def obtenerMedia(muestra):
    suma = 0
    for i in muestra:
        suma += i
    return suma / len(muestra)

def obtenerVarianza(muestra):
    sumatoria = 0
    media = obtenerMedia(muestra)
    for i in muestra:
        sumatoria += (i - media) ** 2
    return (1/(len(muestra)-1)) * sumatoria


def obtenerDesEst(muestra):
    sumatoria = 0
    media = obtenerMedia(muestra)
    for i in muestra:
        sumatoria += (i - media) ** 2
    return math.sqrt((1/(len(muestra)-1)*(sumatoria)))

