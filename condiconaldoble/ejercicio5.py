import os
#declarar variables
cliente,numero_de_empanadas,precio_de_empanada="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_empanadas=int(os.sys.argv[2])
precio_de_empanada=float(os.sys.argv[3])

#processing
costo_empanada=(numero_de_empanadas*precio_de_empanada)
verificador=(costo_empanada>40)

if(costo_empanada>40):
    print("nuestra panaderia esta encantada por su compra")
else:
    print("Gracias por la compra")
