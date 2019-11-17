import os
#declarar variables
cliente,numeros_de_polos,precio_de_polo="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numeros_de_polos=int(os.sys.argv[2])
precio_de_polo=float(os.sys.argv[3])

#processing
costo_polo=(numeros_de_polos*precio_de_polo)
verificador=(costo_polo>400)

if(costo_polo>400):
    print("Ud gano un descuento del %20")
