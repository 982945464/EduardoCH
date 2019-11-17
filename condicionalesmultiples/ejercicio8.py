import os
#declarar variables

cliente,numero_de_cremoladas,precio_de_cremolada="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_cremoladas=int(os.sys.argv[2])
precio_de_cremolada=float(os.sys.argv[3])

#processing
costo_cremolada=(numero_de_cremoladas*precio_de_cremolada)
verificador=(costo_cremolada>100)

#si_el_costo_de_las_cremoladas_es_mayor_que_100_al_cliente_le_dara_gripe
#si_el_costo_de_las_cremoladas_es_menor_que_100_al_cliente_se_quedara_con_sed
#si_el_costo_de_las_cremoladas_es_igual_que_100_al_cliente_se_quedara_satisfecho

if(costo_cremolada>100):
    print("al cliente le dara gripe")

if(costo_cremolada<100):
    print("el cliente se quedara con sed")

if(costo_cremolada==100):
    print("el cliente quedara satisfecho")

#fin_if
