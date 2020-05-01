import time
import math
import random

def tiempoEnQueSeDesocupaLaEstacion(estacion):
    return estacion[1]

n_clientes = int(raw_input("Numero de clientes: "))
t_entre_llegada  = int(raw_input("Tiempo entre llegadas: "))
t_servicio_min = int(raw_input("Tiempo minimo de servicio: "))
t_servicio_max = int(raw_input("Tiempo maximo de servicio: "))
n_estaciones = int(raw_input("Numero de estaciones de servicio: "))

t_llegada = 0
estaciones = []
servicios = []

for e in range(0, n_estaciones):
    # [numero de estacion, tiempo en el que se va a desocupar]
    estaciones.append([e+1, 0])

for i in range(0, n_clientes):
    t_llegada += int(-t_entre_llegada*math.log(random.random()))
    t_servicio = int(t_servicio_min+(t_servicio_max-t_servicio_min)*random.random())
    t_salida = t_llegada + t_servicio

    # se ordenan las estaciones de menos a mayor con respecto al tiempo de salida
    # el tiempo de salida viene siendo el tiempo para el que estaran desocupadas
    # aka. tiempo de salida del cliente anterior
    estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)

    # el tiempo de espera se calcula tomando el tiempo en el que se desocupa la estacion
    # mas proxima menos el tiempo de llegada actual
    t_espera = estaciones[0][1] - t_llegada

    # si el tiempo en el que se desocupo la estacion es menor que el de llegada
    # la espera es 0
    if t_espera < 0:
        t_espera = 0

    t_salida += t_espera
    estaciones[0][1] = t_salida

    servicios.append([i+1, t_llegada, t_salida, estaciones[0][0], t_espera])

    print "Cliente #%s Llegada: %s Espera: %s Servicio: %s Salida: %s Estacion: %s" %(i+1, t_llegada, t_espera, t_servicio, t_salida, estaciones[0][0])

estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
t_salida_ultimo = estaciones[-1][1]
n_estaciones_ocupadas = 0
n_clientes_en_espera = 0

raw_input("Presiona enter para iniciar con la simulacion (%s segundos)..." %(t_salida_ultimo))

for t in range(0, t_salida_ultimo+1):
    mensaje = "%s: (%s/%s) ESTACIONES EN SERVICIO, %s CLIENTES EN ESPERA" %(t, n_estaciones_ocupadas, n_estaciones, n_clientes_en_espera)

    for servicio in servicios:
        if servicio[1] == t:
            mensaje += "\n >>> LLEGA: cliente #%s SERA ATENDIDO EN ESTACION: #%s" %(servicio[0],servicio[3])
            if n_estaciones_ocupadas < n_estaciones:
                n_estaciones_ocupadas += 1

            if servicio[4] > 0:
                n_clientes_en_espera += 1

        elif servicio[2] == t:
            mensaje += "\n <<< SALE:  cliente #%s %s min DE ESPERA, SE DESOCUPA ESTACION: #%s" %(servicio[0], servicio[4], servicio[3])
            if n_estaciones_ocupadas > 0 and n_clientes_en_espera == 0:
                n_estaciones_ocupadas -= 1

            if n_clientes_en_espera > 0:
                n_clientes_en_espera -= 1

    print mensaje
    time.sleep(1)
