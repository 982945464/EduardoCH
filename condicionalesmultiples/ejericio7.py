import os
#declarar variables
cliente,numeros_de_polos,precio_de_polo="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numeros_de_polos=int(os.sys.argv[2])
precio_de_polo=float(os.sys.argv[3])

#processing
costo_polo=(numeros_de_polos*precio_de_polo)
verificador=(costo_polo>400)

#si_el_precio_del_polo_supera_los_400_ganara_un_descueto_de_%20
#si_el_precio_del_polo_no_supera_los_400_no_ganara_descuento
#si_el_precio_del_polo_es_igual_a_400_ganara_descuento_de_%10

if(costo_polo>400):
    print("Ud gano un descuento del %20")

if(costo_polo<400):
    print("no gano ningun descuento")

if(costo_polo==400):
    print("Ud gano un descuento del %10")

#fin_if
