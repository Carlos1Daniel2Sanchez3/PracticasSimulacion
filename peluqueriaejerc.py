import math 
import random 

R1 = []
R2 = []
N_llegadas = []
llegadas = []
cortes = []
salidas = []
esperas = []
listaClientes = []

Num_cliente = int(input('Numero de clientes : '))
Tmin_Corte = int(input('Tiempo minimo de corte: '))
Tmax_Corte = int(input('Tiempo maximo de corte: '))
Tentre = int(input('Tiempo entre llegada de los clientes: '))

for i in range(0,Num_cliente):
    num1 = random.random()
    R1.append(num1)
    num2 = random.random()
    R2.append(num2)

Tllegada_acumulado = 0

for i in range(0,Num_cliente):
	t_llegada = - Tentre*(math.log(R1[i]))
    	Tllegada_acumulado += t_llegada

	llegadas.append(Tllegada_acumulado)

	t_corte = (Tmin_Corte + ((Tmax_Corte-Tmin_Corte)*(R2[i])))
    	cortes.append(t_corte)

	if i == 0:
		espera = 0
	else:
        	espera = salidas[i-1] - llegadas[i]
        	if espera <= 0:
            		espera = 0
       		else:
           		espera = espera
	esperas.append(espera)

	if i == 0:
		salida = llegadas[i] + cortes[i]
	else:
		salida = llegadas[i] + cortes[i] + esperas[i]

	salidas.append(salida)

	listaCliente = llegadas[i], cortes[i],salidas[i],esperas[i]
	listaClientes.append(listaCliente)

print("\n\n Aleatorios1: "+ str(R1) + " ,\nAleatorios2: " + str(R2))
print("\n\n\n+---------------------------------------------------------------------------------+\n\
| Cliente   T_llegada            T_corte              T_salida             T_espera   |\n\
|----------------------------------------------------------------------------------   |")
TesperaTotal = 0
corteTotal = 0
for j in range(0,Num_cliente):
	print("|    %s           %.2f              %.2f              %.2f               %.2f  |" %(j, llegadas[j],cortes[j],salidas[j],esperas[j]))
	TesperaTotal += esperas[j]

	T_salidaUltimoCliente = salidas[j]
	corteTotal += cortes[j]
	
	
print("\n salida ultimocliente : %.2f"%T_salidaUltimoCliente)
print("esperatotal: %.2f" %TesperaTotal)
print("tiempo de corte total : %.2f" %corteTotal)

fila_Longitud = T_salidaUltimoCliente / TesperaTotal
print("\n\nlongitud promedio de la fila es %.2f" %fila_Longitud)

t_promedioEspera = TesperaTotal / Num_cliente
print("tiempo promedio de espera  es de %.2f" %t_promedioEspera)

usoInstalacion = corteTotal / T_salidaUltimoCliente
instalacion = usoInstalacion* 100
print("Las instalaciones se usaron en un %.2f %%" %instalacion)





