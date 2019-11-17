import os
#declarar variables
cliente,numeros_de_zapatillas,precio_de_zapatilla="",0.0,0.0
verficador= False

#input
cliente=os.sys.argv[1]
numeros_de_zapatillas=int(os.sys.argv[2])
precio_de_zapatilla=float(os.sys.argv[3])

#processing
costo_zapatilla=(numeros_de_zapatillas*precio_de_zapatilla)
verificador=(costo_zapatilla>400)

#si_el_costo_de_la_zapatilla_es_mayor_que_400_ganara_una_mochila
#si_el_costo_de_la_zapatilla_es_menor_que_400_no_ganara_nada
#si_el_costo_de_la_zapatilla_es_igual_que_400_ganara_una_cartuchera

if(costo_zapatilla>400):
    print("oferta: ud. ha ganado una mochila")

if(costo_zapatilla<400):
    print("Ud no ha ganado nada")

if(costo_zapatilla==400):
    print("Ud ha ganado una cartuchera")

#fin_if
