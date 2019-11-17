import os
#declarar variables

consultora,numero_de_productos,precio_de_producto="",0.0,0.0
verificador= False

#input
consultora=os.sys.argv[1]
numero_de_productos=int(os.sys.argv[2])
precio_de_producto=float(os.sys.argv[3])

#processing
costo_producto=(numero_de_productos*precio_de_producto)
verificador=(costo_producto>70)

#si_el_costo_del_producto_es_mayor_que_70_el_comprador_sera_excesivo
#si_el_costo_del_producto_es_menor_que_70_el_comprador_sera_tacaño
#si_el_costo_del_producto_es_igual_que_70_el_comprador_sera_moderado

if(costo_producto>70):
    print("UD es un comprador excesivo")

if(costo_producto<70):
    print("Ud es un comprador tacaño")

if(costo_producto==70):
    print("Ud es un comprador moderado")

#fin_if
