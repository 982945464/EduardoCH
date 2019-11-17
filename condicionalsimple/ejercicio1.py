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

if(costo_producto>70):
    print("UD es un comprador excesivo")
