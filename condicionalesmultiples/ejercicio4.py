import os
#declarar variables
cliente,numero_de_chocolates,precio_de_chocolate="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_chocolates=int(os.sys.argv[2])
precio_de_chocolate=float(os.sys.argv[3])

#processing
costo_chocolate=(numero_de_chocolates*precio_de_chocolate)
verificador=(costo_chocolate>100)

#si_el_costo_del_chocolate_es_mayor_que_100_ganara_dos_entradas_para_el_cine
#si_el_costo_del_chocolate_es_menor_que_100_no_ganara_nada
#si_el_costo_del_chocolate_es_igual_que_100_ganara_solo_una_entrada

if(costo_chocolate>100):
    print("Ud gano dos entradas para el cine")

if(costo_chocolate<100):
    print("Ud no gano nada")

if(costo_chocolate==100):
    print("Ud gano una entrada para el cine")

#fin_if
