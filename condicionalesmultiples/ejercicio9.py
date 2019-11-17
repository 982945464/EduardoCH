import os
#declarar variables

comprador,numeros_de_botellas_de_vino,precio_de_cada_vino="",0.0,0.0
verificador= False

#input
comprador=os.sys.argv[1]
numeros_de_botellas_de_vino=int(os.sys.argv[2])
precio_de_cada_vino=float(os.sys.argv[3])

#processing
precio_botella=(numeros_de_botellas_de_vino*precio_de_cada_vino)
verificador=(precio_botella>200)

#si_el_precio_de_la_botella_es_mayor_que_100_ganara_un_vale_de_100_soles
#si_el_precio_de_la_botella_es_menor_que_100_se_le_dara_las_gracias_por_la_compra
#si_el_precio_de_la_botella_es_igual_que_100_ganara_un_vale_de_50_soles

if(precio_botella>200):
    print("Ha ganado un vale por 100 soles")

if(precio_botella<200):
    print("Gracias por su compra")

if(precio_botella==200):
    print("Ha ganado una val por 50 soles")

#fin_if
