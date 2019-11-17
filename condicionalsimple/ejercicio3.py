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

if(costo_cremolada>100):
    print("Gracias por su compra")
