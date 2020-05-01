import random
import math
import time 

#logaritmo natural = math.log()

def tiempoEnQueSeDesocupaLaEstacion(estacion):#_______________________
    return estacion[1]#___________________________________

t_entre_llegada = int(raw_input("INGRESA TIEMPO ENTRE LLEGADA:    "))
t_minimo = int(raw_input("TIEMPO MINIMO EN CORTE:    "))
t_maximo = int(raw_input("TIEMPO MAXIMO EN CORTE:    "))
total_de_clientes = int(raw_input("TOTAL DE CLIENTES:     "))
barbeross = int(raw_input("Numero de peluqueros:   "))

t_llegada_total = 0
t_salida_anterior = 0
espera_total_1 = 0
t_corte_1 = 0

tiempo_llegada = []
tiempo_corte = []
cli = []
sali = []
espe = []
tiempo_llegada_entero = []
sali_entero = []

estaciones = []#___________________________________
barbero = []#_______________________
birbero = []

for e in range(0, barbeross):#_______________________________
    estaciones.append([e+1, 0])#_____________________________-

for i in range(total_de_clientes):
	R = random.random()
	t_llegada = abs((((-1)*(t_entre_llegada))*((math.log(R)))))#tiempo de llegada de un solo cliente
	t_llegada_total = t_llegada + t_llegada_total # tiempo de llegada sumado
	tiempo_llegada.append(t_llegada_total) #agregar el tiempo de llegada a la lista
	tiempo_llegada_entero.append(int(t_llegada_total))
	t_corte = ((t_minimo + ((t_maximo - t_minimo) * (R)))) #tiempo de corte
	tiempo_corte.append(t_corte)
	cli.append(i) #numrto de cliente agregado a la lista
	t_salida = t_llegada_total + t_corte # tiempo de salida 
	sali.append(t_salida)
	sali_entero.append(int(t_salida))
	espera_total = (t_salida_anterior - t_llegada_total)
	estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
	# el tiempo de espera se calcula tomando el tiempo en el que se desocupa la estacion
	# mas proxima menos el tiempo de llegada actual
	espera_total = estaciones[0][1] - t_llegada_total
	espe.append(espera_total)
	# si el tiempo en el que se desocupo la estacion es menor que el de llegada
	# la espera es 0
	if espera_total < 0:
		espera_total = 0
	t_salida += espera_total
	estaciones[0][1] = t_salida_anterior

	barbero.append([i+1, t_llegada_total, t_salida, estaciones[0][0], espera_total])

	#nuestro codigo
	t_salida_anterior = t_salida
	
	espera_total_1 = espera_total + espera_total_1
	t_corte_1 = (t_corte) + (t_corte_1)
	#codigo anterior nuestro
sep = '|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*16, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |   SALIDA       |    PELUQUERO    |     ESPERA     |\n{0}'.format(sep))
for b in barbero:
	n_cliente = b[0]
	t_llegada = b[1]
	tiempo = b[2]
	barb = b[3]
	espera = b[4]
	print('| {:>8.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} | {:>14.2f} |'.format(n_cliente, t_llegada,tiempo,barb, espera,sep))
	birbero.append(barb)


estaciones.sort(key=tiempoEnQueSeDesocupaLaEstacion)
t_salida_ultimo = estaciones[-1][1]
n_estaciones_ocupadas = 0
n_clientes_en_espera = 0
#________________________________________________________________________________




long_de_fila = (espera_total_1) / (t_salida_anterior) 
t_espera_promedio = (espera_total_1) / (total_de_clientes)
uso_instalacion = (t_corte_1) / (t_salida_anterior) 

print ("LONGITUD PROMEDIO DE FILA   %.2f" %(long_de_fila))
print ("TIEMPO DE ESPERA PROMEDIO     %.2f" %(t_espera_promedio))
print ("USO PROMEDIO DE LA INSTALACION      %.2f" %(uso_instalacion))

raw_input("tiempo de simulcacion (%ssegundos) " %(int(t_salida_anterior)))
for t in range(0, int(t_salida_anterior+1)):
    mensaje = "%s: (%s/%s) ESTACIONES EN SERVICIO, %s CLIENTES EN ESPERA" %(t, n_estaciones_ocupadas, barbeross, n_clientes_en_espera)

    for b in barbero:
        if int (b[1]) == t:
            mensaje += "\n >>> LLEGA: cliente #%s SERA ATENDIDO EN ESTACION: #%s" %(b[0],b[3])
            if n_estaciones_ocupadas < barbeross:#cambiar n_estaciones por barberos 
                n_estaciones_ocupadas += 1

            if b[4] > 0:
                n_clientes_en_espera += 1

        elif int(b[2]) == t:
            mensaje += "\n <<< SALE:  cliente #%s %s min DE ESPERA, SE DESOCUPA ESTACION: #%s" %(b[0], b[4], b[3])
            if n_estaciones_ocupadas > 0 and n_clientes_en_espera == 0:
                n_estaciones_ocupadas -= 1

            if n_clientes_en_espera > 0:
                n_clientes_en_espera -= 1

    print mensaje
    time.sleep(1)


exit()
