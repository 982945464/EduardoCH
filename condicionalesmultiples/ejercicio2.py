import os
#declarar variables
cliente,numero_de_helados,precio_de_helado="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_helados=int(os.sys.argv[2])
precio_de_helado=float(os.sys.argv[3])

#processing
costo_helado=(numero_de_helados*precio_de_helado)
verificador=(costo_helado>150)

#si_el_costo_de_los_helados_es_mayor_que_150_agradecer_de_parte_de_la_empresa_donofrio
#si_el_costo_de_los_helados_es_menor_que_150_darle_solo_las_gracias
#si_el_costo_de_los_helados_es_igual_que_150_agradecer_de_de_parte_del_vendedor



if(costo_helado>150):
    print("donofrio agradece su pedido")

if(costo_helado<150):
    print("Gracias")

if(costo_helado==150):
    print("muchas gracias de mi parte")

#fin_if
