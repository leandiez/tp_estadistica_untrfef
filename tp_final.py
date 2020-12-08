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

#Genera un par de numeros aleatorios con el metodo Box-Muller y elije uno para retornar aleatoriamente con bernouli p=0.5
def randomNormalDist(paramMu, paramSigma):
    random1 = random.random()
    random2 = random.random()
    selector = randomBernouli(0.5)
    normal01 = ((math.sqrt(-2 * math.log(random1)) * math.cos(2 * math.pi * random1))*paramSigma)+paramMu
    normal02 = ((math.sqrt(-2 * math.log(random2)) * math.sin(2 * math.pi * random2))*paramSigma)+paramMu
    if selector > 0.5:
        return normal01
    return normal02



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

# Parte 2: Estadistica descriptiva

def ejercicio22():
    #Generacion de muestras
    muestra1 = [randomExp(0.5) for i in range(10)]
    print("Media de muestra 1: " + str(obtenerMedia(muestra1)))
    print("Varianza de muestra 1: "+ str(obtenerVarianza(muestra1)))

    muestra2 = [randomExp(0.5) for i in range(30)]
    print("Media de muestra 2: " + str(obtenerMedia(muestra2)))
    print("Varianza de muestra 2: "+ str(obtenerVarianza(muestra2)))

    muestra3 = [randomExp(0.5) for i in range(200)]
    print("Media de muestra 3: " + str(obtenerMedia(muestra3)))
    print("Varianza de muestra 3: "+ str(obtenerVarianza(muestra3)))


    #Creacion del espacio de graficos y graficos
    fig, axs = plt.subplots(3, 3)

    # La funcion histograma se encarga de realizar la cuenta de frecuencias segun la cantidad de bins que se quieran declarar.
    # Posteriormente para que la cuenta sea relativa se usa el parametro weights el cual asigna a cada columna un peso relativo a 1
    # https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html?highlight=hist#matplotlib.axes.Axes.hist
    axs[0][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.4)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))
    axs[1][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.2)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))
    axs[2][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.1)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))

    axs[0][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.4)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))
    axs[1][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.2)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))
    axs[2][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.1)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))

    axs[0][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.4)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))
    axs[1][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.2)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))
    axs[2][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.1)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))
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

    #Calculo medias y desviaciones estandar muestrales
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

    fig, axs = plt.subplots(2, 2, sharey=True)

    axs[0][0].hist(muestra1prima, bins="auto")
    axs[0][1].hist(muestra2prima, bins="auto")
    axs[1][0].hist(muestra3prima, bins="auto")
    axs[1][1].hist(muestra4prima, bins="auto")
    plt.show()


# Parte 4: Estadistica inferencial
muestra1 = [randomNormalDist(100,5) for i in range(10)]
muestra2 = [randomNormalDist(100,5) for i in range(30)]

print(muestra1)
print(muestra2)

## 4.4 Obtener el limite inferior de varianza usando estimador chi-cuadrado
## Calcular el error de tipo 2 con la varianza muestral limite de la hipotesis alternativa
## Calcular la probabilidad de que el nuevo chi-cuadrado usando el valor de tabla

""" 
[8:31, 5/12/2020] Alejandro Araneda UNTREF: Lo único que yo le dije fue
[8:32, 5/12/2020] Alejandro Araneda UNTREF: Vos tenés un estimador (como pueder el promedio) que se llama Chi cuadrado.
[8:32, 5/12/2020] Alejandro Araneda UNTREF: Ese Chi cuadrado suponiendo población normal, es (n-1)s^2/sigma^2
[8:32, 5/12/2020] Alejandro Araneda UNTREF: La distribución de probabilidad de ese estimador es la distribución Chi cuadrado.
[8:32, 5/12/2020] Alejandro Araneda UNTREF: (Así como el promedio de una muestra de población normal, seguía una distribución normal si sabés sigma, o t de Student si no sabés sigma)
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Despejado, tenés entonces los  límites laterales y el intervalo de confianza.
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Sigma^2 es mayor a X con 1-alfa de confianza si (n-1)s^2/Chi(gl = n-1, p=1-alfa) es mayor a X
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Volviendo a despejar: Sigma^2 es mayor a X con 1-alfa de confianza si s^2 es mayor a X*Chi(gl=n-1, p=1-alfa)/(n-1)
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Esto fue lo que hicimos en el TP
[8:33, 5/12/2020] Alejandro Araneda UNTREF: El Chi como es una proporción entre s y sigma, cuanto más grande sea, en particular mayor a n-1, significa que s es mayor a sigma.
[8:33, 5/12/2020] Alejandro Araneda UNTREF: por eso el límite inferior usa 1-alfa (el chi más grande) y el límite inferior es alfa (el Chi más chico)
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Volviendo al test de hipótesis, efectivamente tenes que buscar una s^2 límite que te hubiera  llevado a rechazar la tesis H0.
[8:33, 5/12/2020] Alejandro Araneda UNTREF: Tenés el Chi (gl=n-1, 1-alfa) lo multiplicas por 5 (sigma de la hipótesis cero) y dividis por n-1 y tenés la s limite que no te hubiera llevado a rechazar sigma>5
[8:33, 5/12/2020] Alejandro Araneda UNTREF: luego con esa s limite vas al revés con la sigma 6 para hallar el chi y su probabilidad
[8:33, 5/12/2020] Alejandro Araneda UNTREF: El enlace que él encontró recién lo leí y es muy explicativo. http://www.itchihuahua.edu.mx/academic/industrial/estadistica1/cap03b.html 
"""