import pygame,sys
from pygame.locals import *


import random
import math
import time 



def tiempoEnQueSeDesocupaLaEstacion(estacion):
    return estacion[1]

t_entre_llegada = int(raw_input("Tiempo entre llegada:    "))
t_minimo = int(raw_input("Tiempo minimo de corte:    "))
t_maximo = int(raw_input("Tiempo maximo de corte:    "))
total_de_clientes = int(raw_input("Total de clientes:     "))
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

estaciones = []
barbero = []
birbero = []
for e in range(0, barbeross):
    estaciones.append([e+1, 0])

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

	
	t_salida_anterior = t_salida
	
	espera_total_1 = espera_total + espera_total_1
	t_corte_1 = (t_corte) + (t_corte_1)
	
sep = '|{}|{}|{}|{}|{}|'.format('-'*10, '-'*16, '-'*16, '-'*16, '-'*16)
print('{0}\n| CLIENTE  |    LLEGADA     |   SALIDA       |     PELUQUERO    |     ESPERA     |\n{0}'.format(sep))
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

long_de_fila = (espera_total_1) / (t_salida_anterior) 
t_espera_promedio = (espera_total_1) / (total_de_clientes)
uso_instalacion = (t_corte_1) / (t_salida_anterior) 

print ("Longitud promedio de fila  %.2f" %(long_de_fila))
print ("Tempo de espera promedio    %.2f" %(t_espera_promedio))
print ("Uso promedio de la instalacion      %.2f" %(uso_instalacion))
raw_input("Tiempo de simulacion (%ssegundos) " %(int(t_salida_anterior)))


pygame.init()

FPS = 10
fpsClock = pygame.time.Clock()


screen = pygame.display.set_mode((866,599))
pygame.display.set_caption('PELUQUERIA')

imageImg  = pygame.image.load('salon.png')
barbero1  = pygame.image.load('peluquero.png')
barbero2  = pygame.image.load('peluquero.png')
cliente  = pygame.image.load('cliente.png')

clientes_en_pantalla = []

t=1
fps_contador = 0
posy = 100
# the main game loop
while True:
	if t == int(t_salida_anterior):
		pygame.quit()
        	sys.exit()

	screen.fill((0,0,0))
    	screen.blit(imageImg, (0, 0))
	screen.blit(barbero1, (0, 0))
	screen.blit(barbero1, (300, 0))

	# mostrar clientes en pantalla
	for c in clientes_en_pantalla:
		if c[5] == True:
			screen.blit(cliente, (c[1], c[2]))

			if c[3] == 1:
				limite = 170

			else:
				limite = 530

			if c[1] < limite and c[4] <= 0:
				c[1]+= 10
				c[4]-= 1

#manda a llamar las imagenes 
	fps_contador += 1
	if fps_contador == 10:
		print "%s/%s" %(t, t_salida_anterior)
		for b in barbero:
			if int (b[1]) == t:
			    clientes_en_pantalla.append([b[0], 0, posy, b[3], b[4], True])
			    posy += 15
			    if n_estaciones_ocupadas < barbeross:
				n_estaciones_ocupadas += 1

			    if b[4] > 0:
				n_clientes_en_espera += 1

			elif int(b[2]) == t:
			    for c in clientes_en_pantalla:
				if c[0] == b[0]:
					c[5] = False

			    if n_estaciones_ocupadas > 0 and n_clientes_en_espera == 0:
				n_estaciones_ocupadas -= 1

			    if n_clientes_en_espera > 0:
				n_clientes_en_espera -= 1

		t += 1
		fps_contador = 0


	for event in pygame.event.get():
    		if event.type == QUIT:
        		pygame.quit()
        		sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)


for t in range(0, int(t_salida_anterior+1)):
    mensaje = "%s: (%s/%s) ESTACIONES EN SERVICIO, %s CLIENTES EN ESPERA" %(t, n_estaciones_ocupadas, barbeross, n_clientes_en_espera)
