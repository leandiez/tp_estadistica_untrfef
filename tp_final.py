import random, math
import matplotlib.pyplot as plt
import numpy as np
import auxi
from scipy.stats import chi2, norm
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
    if selector:
        return normal01
    return normal02



# Parte 2: Estadistica descriptiva

def ejercicio22():
    #Generacion de muestras
    muestra1 = [randomExp(0.5) for i in range(10)]
    print("Media de muestra 1: " + str(auxi.obtenerMedia(muestra1)))
    print("Varianza de muestra 1: "+ str(auxi.obtenerVarianza(muestra1)))

    muestra2 = [randomExp(0.5) for i in range(30)]
    print("Media de muestra 2: " + str(auxi.obtenerMedia(muestra2)))
    print("Varianza de muestra 2: "+ str(auxi.obtenerVarianza(muestra2)))

    muestra3 = [randomExp(0.5) for i in range(200)]
    print("Media de muestra 3: " + str(auxi.obtenerMedia(muestra3)))
    print("Varianza de muestra 3: "+ str(auxi.obtenerVarianza(muestra3)))


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
    media11 = auxi.obtenerMedia(muestra11)
    desv11 = auxi.obtenerDesEst(muestra11)
    print("3.2 La media de la muestra 1 binomial es: "+ str(media11))
    print("3.2 La desviacion estandar de la muestra 1 binomial es: "+str(desv11))

    media22 = auxi.obtenerMedia(muestra22)
    desv22 = auxi.obtenerDesEst(muestra22)
    print("3.2 La media de la muestra 2 binomial es: "+str(media22))
    print("3.2 La desviacion estandar de la muestra 2 binomial es: "+str(desv22))

    media33 = auxi.obtenerMedia(muestra33)
    desv33 = auxi.obtenerDesEst(muestra33)
    print("3.2 La media de la muestra 3 binomial es: "+str(media33))
    print("3.2 La desviacion estandar de la muestra 3 binomial es: "+str(desv33))

    media44 = auxi.obtenerMedia(muestra44)
    desv44 = auxi.obtenerDesEst(muestra44)
    print("3.2 La media de la muestra 4 binomial es: "+str(media44))
    print("3.2 La desviacion estandar de la muestra 4 binomial es: "+str(desv44))

    #Normalizacion de las muestras
    #
    muestra1prima = [((x-media11)/desv11) for x in muestra11]
    muestra2prima = [((x-media22)/desv22) for x in muestra22]
    muestra3prima = [((x-media33)/desv33) for x in muestra33]
    muestra4prima = [((x-media44)/desv44) for x in muestra44]

    print("La media de la muestra normalizada 1 es: " + str(auxi.obtenerMedia(muestra1prima))) 
    print("La media de la muestra normalizada 2 es: " + str(auxi.obtenerMedia(muestra2prima))) 
    print("La media de la muestra normalizada 3 es: " + str(auxi.obtenerMedia(muestra3prima)))
    print("La media de la muestra normalizada 4 es: " + str(auxi.obtenerMedia(muestra4prima)))

    fig, axs = plt.subplots(2, 2, sharey=True)

    axs[0][0].hist(muestra1prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra1prima)+1./len(muestra1prima))
    axs[0][1].hist(muestra2prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra2prima)+1./len(muestra2prima))
    axs[1][0].hist(muestra3prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra3prima)+1./len(muestra3prima))
    axs[1][1].hist(muestra4prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra4prima)+1./len(muestra4prima))

    axs[0][0].set_title("Muestra 1 Normalizada")
    axs[0][1].set_title("Muestra 2 Normalizada")
    axs[1][0].set_title("Muestra 3 Normalizada")
    axs[1][1].set_title("Muestra 4 Normalizada")
    plt.show()


# Parte 4: Estadistica inferencial

def ejercicio44():
    muestra2 = [randomNormalDist(100,math.sqrt(5)) for i in range(30)]
    #Obtengo mi limite inferior para el intervalo de confianza de la varianza. 
    #Chi2 se obtiene mediante 1-alfa igual a 0.01 y el grado de libertad n-1
    valor_critico_chi2 = chi2.ppf(0.01, len(muestra2) - 1)
    print("Valor de varianza muestra: "+str(auxi.obtenerVarianza(muestra2)))
    print("Valor calculado de la prueba usando chi-cuadrado:" +str((5/(len(muestra2)-1))*valor_critico_chi2))

## 4.4 Obtener el limite inferior de varianza usando estimador chi-cuadrado
## Calcular el error de tipo 2 con la varianza muestral limite de la hipotesis alternativa
## Calcular la probabilidad de que el nuevo chi-cuadrado usando el valor de tabla


def ejercicio45():
    muestra2 = [randomNormalDist(100,math.sqrt(5)) for i in range(30)]
    franjas = np.arange(min(muestra2), max(muestra2), 0.5)
    frecuencias = [len([x for x in muestra2 if x >= i and x < i + 0.5]) for i in franjas]

    #Genero la frecuencia ideal usando la funcion normal de SciPy
    def generar_frecuencia_ideal(x):
        return round((norm.cdf(x + 0.5, loc=100, scale=math.sqrt(5)) - norm.cdf(x, loc=100, scale=math.sqrt(5))) * 30)

    frecuencias_ideales = [generar_frecuencia_ideal(x) for x in franjas]
    print(frecuencias)
    print(frecuencias_ideales)

    nuevas_frecuencias = []
    nuevas_frecuencias_ideales = []
    acumulado = 0
    acumulado_ideal = 0
    for i in range(len(frecuencias)):
        acumulado += frecuencias[i]
        acumulado_ideal += frecuencias_ideales[i]
        if (acumulado >= 5 and acumulado_ideal >= 5):
            nuevas_frecuencias.append(acumulado)
            nuevas_frecuencias_ideales.append(acumulado_ideal)
            acumulado = 0
            acumulado_ideal = 0
    print(nuevas_frecuencias)
    print(nuevas_frecuencias_ideales)

    def calcular_error_cuadratico(frec, nuevas_frec):
        for i in frec:
            for j in nuevas_frec:
                yield (((i-j)**2)/j)
        return

    error2 = sum(calcular_error_cuadratico(nuevas_frecuencias, nuevas_frecuencias_ideales))
    print("Error de la prueba de ajuse: "+str(error2))
    print(("Valor critico de chi2: "))
    print(chi2.ppf(0.01, len(nuevas_frecuencias_ideales) - 1))

    print("¿El valor del error cuadratico es mayor al de chi-cuadrado con 0.01 de alfa?")
    print(error2 > chi2.ppf(0.01, len(nuevas_frecuencias_ideales) - 1))

ejercicio45()