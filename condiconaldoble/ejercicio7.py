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

if(costo_chocolate>100):
    print("Ud gano dos entradas para el cine")
else:
    print("Ud gano una entrada para el cine")
