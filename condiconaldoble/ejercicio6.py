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

if(costo_cuaderno>120):
    print("Ud gano un vale de compra de utiles escolares")
else:
    print("Siga intentando")
