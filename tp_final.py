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
    muestra2 = generarExp5(30)
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

muestra1 = [randomBinomial(10 , 0.4) for i in range(100)]
print(muestra1)
muestra2 = [randomBinomial(20 , 0.4) for i in range(100)]
print(muestra2)
muestra3 = [randomBinomial(50 , 0.4) for i in range(100)]
print(muestra3)
muestra4 = [randomBinomial(100 , 0.4) for i in range(100)]
print(muestra4)

fig, axs = plt.subplots(2, 2, sharey=True, tight_layout=True)

axs[0][0].hist(muestra1, bins=max(muestra1))
axs[0][1].hist(muestra2, bins=max(muestra2))
axs[1][0].hist(muestra3, bins=max(muestra3))
axs[1][1].hist(muestra4, bins=max(muestra4))
plt.show()

# Muestras distribucion binomial de tamaño 200
muestra11 = [randomBinomial(10 , 0.4) for i in range(200)]
muestra22 = [randomBinomial(20 , 0.4) for i in range(200)]
muestra33 = [randomBinomial(50 , 0.4) for i in range(200)]
muestra44 = [randomBinomial(100 , 0.4) for i in range(200)]
#Normalizacion de las muestras
muestra21 = [randomNormalDist((10*0.4), (10*0.4*0.6)) for i in range(200)]
muestra22 = [randomNormalDist((20*0.4), (20*0.4*0.6)) for i in range(200)]
muestra23 = [randomNormalDist((50*0.4), (50*0.4*0.6)) for i in range(200)]
muestra24 = [randomNormalDist((50*0.4), (50*0.4*0.6)) for i in range(200)]


# Parte 4:
