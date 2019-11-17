import os
#declarar variables
cliente,numero_de_cuadernos,precio_de_cuaderno="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_cuadernos=int(os.sys.argv[2])
precio_de_cuaderno=float(os.sys.argv[3])

#processing
costo_cuaderno=(numero_de_cuadernos*precio_de_cuaderno)
verificador=(costo_cuaderno>120)

#si_el_costo_del_cuaderno_es_mayor_que_120_ganara_una_vale_de_compra_de_utiles_escolares
#si_el_costo_del_cuaderno_es_menor_que_120_se_le_dira_que_siga_intentando
#si_el_costo_del_cuaderno_es_igual_que_120_ganara_solo_un_descuento_de_%10

if(costo_cuaderno>120):
    print("Ud gano un vale de compra de utiles escolares")

if(costo_cuaderno<120):
    print("Siga intentando")

if(costo_cuaderno==120):
    print("Ud gano un descuento del %10")

#fin_if
