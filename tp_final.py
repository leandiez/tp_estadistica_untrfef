import random, math
import matplotlib.pyplot as plt
import numpy as np

#Parte 1: Simulacion

#Devuelve un exito (1) o fracaso (0) dependiendo de la probabilidad de exito p
def randomBernouli(p):
    if random.random() <= p:
        return 1
    return 0

#Devuelve cantidad de exitos Bernouli repitiendo n veces el experimento
def randomBinomial(n,p):
    exitos = 0
    for experimento in range(n-1):
        if randomBernouli(p) == 1:
            exitos += 1
    return exitos

def randomExp(paramLambda):
    return (math.log(random.random())/paramLambda)*-1

def randomNormalDist(paramMu, paramSigma):
    normal01 = math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random())
    return (paramMu + paramSigma*normal01)

def testParteUno():
    pass

#Funciones auxiliares

def obtenerMedia(muestra):
    suma = 0
    for i in muestra:
        suma += i
    return suma / len(muestra)

def obtenerVarianza(muestra):
    sumatoria = 0
    for i in muestra:
        sumatoria += (i - obtenerMedia(muestra)) ** 2
    return (1/len(muestra)) * sumatoria


def obtenerDesEst(muestra):
    sumatoria = 0
    for i in muestra:
        sumatoria += (i - obtenerMedia(muestra)) ** 2
    return math.sqrt((1/len(muestra)*(sumatoria)))

# Parte 2
def generarExp5(n):
    miArray = []
    while n > 0:
        miArray.append(randomExp(0.5))
        n = n-1
    return miArray

def ejercicio22():
    #Generacion de muestras
    muestra1 = generarExp5(10)
    print("Media de muestra 1: " + obtenerMedia(muestra1))
    print("Varianza de muestra 1: "+ obtenerVarianza(muestra1))

    muestra2 = generarExp5(30)
    print("Media de muestra 2: " + obtenerMedia(muestra2))
    print("Varianza de muestra 2: "+ obtenerVarianza(muestra2))

    muestra3 = generarExp5(200)

    #Creacion del espacio de graficos y graficos
    fig, axs = plt.subplots(3, 3, sharey=True, tight_layout=True)

    axs[0][0].hist(muestra1, bins=int(int(max(muestra1)) / 0.4), density=True)
    axs[1][0].hist(muestra1, bins=int(int(max(muestra1)) / 0.2), density=True)
    axs[2][0].hist(muestra1, bins=int(int(max(muestra1)) / 0.1), density=True)

    axs[0][1].hist(muestra2, bins=int(int(max(muestra2)) / 0.4), density=True)
    axs[1][1].hist(muestra2, bins=int(int(max(muestra2)) / 0.2), density=True)
    axs[2][1].hist(muestra2, bins=int(int(max(muestra2)) / 0.1), density=True)

    axs[0][2].hist(muestra3, bins=int(int(max(muestra3)) / 0.4), density=True)
    axs[1][2].hist(muestra3, bins=int(int(max(muestra3)) / 0.2), density=True)
    axs[2][2].hist(muestra3, bins=int(int(max(muestra3)) / 0.1), density=True)
    plt.show()

#Parte 3: Convergencia

def ejercicio31():
    muestra1 = [randomBinomial(10 , 0.4) for i in range(100)]
    #print(muestra1)
    muestra2 = [randomBinomial(20 , 0.4) for i in range(100)]
    #print(muestra2)
    muestra3 = [randomBinomial(50 , 0.4) for i in range(100)]
    #print(muestra3)
    muestra4 = [randomBinomial(100 , 0.4) for i in range(100)]
    #print(muestra4)

    #Instancio la figura y los ejes dentro de esa figura
    fig, axs = plt.subplots(2, 2, sharey=True, tight_layout=True)
    #Asigno que muestra se refleja en cada eje
    axs[0][0].hist(muestra1, bins=max(muestra1))
    axs[0][1].hist(muestra2, bins=max(muestra2))
    axs[1][0].hist(muestra3, bins=max(muestra3))
    axs[1][1].hist(muestra4, bins=max(muestra4))
    plt.show()

def ejercicio32Y33():
    # Muestras distribucion binomial de tamaño 200
    muestra11 = [randomBinomial(10 , 0.4) for i in range(200)]
    muestra22 = [randomBinomial(20 , 0.4) for i in range(200)]
    muestra33 = [randomBinomial(50 , 0.4) for i in range(200)]
    muestra44 = [randomBinomial(100 , 0.4) for i in range(200)]

    media11 = obtenerMedia(muestra11)
    desv11 = obtenerDesEst(muestra11)
    print("3.2 La media de la muestra 1 binomial es: "+ str(media11))
    print("3.2 La desviacion estandar de la muestra 1 binomial es: "+str(desv11))

    media22 = obtenerMedia(muestra22)
    desv22 = obtenerDesEst(muestra22)
    print("3.2 La media de la muestra 2 binomial es: "+str(media22))
    print("3.2 La desviacion estandar de la muestra 2 binomial es: "+str(desv22))

    media33 = obtenerMedia(muestra33)
    desv33 = obtenerDesEst(muestra33)
    print("3.2 La media de la muestra 3 binomial es: "+str(media33))
    print("3.2 La desviacion estandar de la muestra 3 binomial es: "+str(desv33))

    media44 = obtenerMedia(muestra44)
    desv44 = obtenerDesEst(muestra44)
    print("3.2 La media de la muestra 4 binomial es: "+str(media44))
    print("3.2 La desviacion estandar de la muestra 4 binomial es: "+str(desv44))

    #Normalizacion de las muestras

    muestra1prima = [((i-media11)/desv11) for i in muestra11]
    muestra2prima = [((i-media22)/desv22) for i in muestra22]
    muestra3prima = [((i-media33)/desv33) for i in muestra33]
    muestra4prima = [((i-media44)/desv44) for i in muestra44]

    print("La media de la muestra normalizada 1 es: " + str(obtenerMedia(muestra1prima))) 
    print("La media de la muestra normalizada 2 es: " + str(obtenerMedia(muestra2prima))) 
    print("La media de la muestra normalizada 3 es: " + str(obtenerMedia(muestra3prima)))
    print("La media de la muestra normalizada 4 es: " + str(obtenerMedia(muestra4prima)))

    fig, axs = plt.subplots(2, 2, sharey=True, tight_layout=True)

    axs[0][0].hist(muestra1prima, bins="auto")
    axs[0][1].hist(muestra2prima, bins="auto")
    axs[1][0].hist(muestra3prima, bins="auto")
    axs[1][1].hist(muestra4prima, bins="auto")
    plt.show()


# Parte 4:
