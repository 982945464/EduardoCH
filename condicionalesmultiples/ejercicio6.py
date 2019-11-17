import os
#declarar variables
cliente,numero_de_empanadas,precio_de_empanada="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_empanadas=int(os.sys.argv[2])
precio_de_empanada=float(os.sys.argv[3])

#processing
costo_empanada=(numero_de_empanadas*precio_de_empanada)
verificador=(costo_empanada>40)

#si_el_costo_de_la_empanada_es_mayor_que_40_ganara_una_canasta_navideña
#si_el_costo_de_la_empanada_es_menor_que_40_se le dara las gracias_por_la_compra
#si_el_costo_de_la_empanada_es_igual_que_40_ganara_un_paneton

if(costo_empanada>40):
    print("Ud gano una canasta navideña")

if(costo_empanada<40):
    print("Gracias por su compra")

if(costo_empanada==40):
    print("Ud gano un paneton")
