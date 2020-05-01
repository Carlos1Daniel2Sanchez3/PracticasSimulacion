import random
import math
import time

R1 = []
R2 = []
n_llegadas = []
cortes = []
llegadas = []
llegadasEnteros = []
salidas = []
salidasEnteros = []
esperas = []
listaClientes = []

No_cliente = int(input('numero de clientes : '))
t_min_Corte = int(input('tiempo minimo de corte: '))
t_max_Corte = int(input('tiempo maximo de corte: '))
t_entre = int(input('tiempo entre llegada de los clientes: '))


for i in range(0,No_cliente):
    num1 = random.random()
    R1.append(num1)
    num2 = random.random()
    R2.append(num2)


t_llegada_acumulado = 0

for i in range(0,No_cliente):
    t_llegada = - t_entre*(math.log(R1[i]))
    t_llegada_acumulado += t_llegada
    
    llegadas.append(t_llegada_acumulado)
    llegadasEnteros.append(int(t_llegada_acumulado))

    # T_CORTE
    t_corte = (t_min_Corte + ((t_max_Corte-t_min_Corte)*(R2[i])))
    cortes.append(t_corte)
   
    # T_ESPERA
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
    salidasEnteros.append(int(salida))
    
    listaCliente = llegadas[i], cortes[i],salidas[i],esperas[i]
    listaClientes.append(listaCliente)
    

print("\n\n RANDOM1: "+ str(R1) + " ,\nRANDOM2: " + str(R2))
print("\n\n\n+---------------------------------------------------------------------------------+\n\
| Cliente   t_llegada            t_corte              t_salida             t_espera|\n\
|----------------------------------------------------------------------------------|")
t_esperaTotal = 0
corteTotal = 0
for j in range(0,No_cliente):
    #print( " | {a}{}      {b}     {c}       {d}       {e}| ".format(a = j,b = llegadas[j],c = cortes[j],d = salidas[j],e = esperas[j]))
    print("|    %s           %.2f              %.2f              %.2f               %.2f  |" %(j, llegadas[j],cortes[j],salidas[j],esperas[j]))
    t_esperaTotal += esperas[j]
    
    t_salidaUltimoCliente = salidas[j]
    corteTotal += cortes[j]


print("\n salida ultimo cliente : %.2f"%t_salidaUltimoCliente)
print("espera total: %.2f" %t_esperaTotal)
print("tiempo de corte total : %.2f" %corteTotal)

fila_Longitud = t_salidaUltimoCliente / t_esperaTotal
print("\n\nlongitud promedio de la fila es %.2f" %fila_Longitud)

t_promedioEspera = t_esperaTotal / No_cliente
print("tiempo promedio de espera  es de %.2f" %t_promedioEspera)

usoInstalacion = corteTotal / t_salidaUltimoCliente
instalacion = usoInstalacion* 100
print("Las instalaciones se usaron en un %.2f %%" %instalacion)

tiempo_maxi = int(t_salidaUltimoCliente)

n_cliente_llegada = 1
n_cliente_salida = 1
for i in range(1,tiempo_maxi+1):
    print("minuto : %d" %i)
    time.sleep(1)
    try:
        if i in llegadasEnteros:
            print("\t\tLlegada del cliente %d " % n_cliente_llegada)
            n_cliente_llegada += 1
        if i in salidasEnteros:
             print("\t\t\t\tsalida del cliente %d " % n_cliente_salida)
             n_cliente_salida += 1
    except ValueError:
        pass
