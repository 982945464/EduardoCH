import os
#declarar variables
cliente,numeros_de_zapatillas,precio_de_zapatilla="",0.0,0.0
verficador= False

#input
cliente=os.sys.argv[1]
numeros_de_zapatillas=int(os.sys.argv[2])
precio_de_zapatilla=float(os.sys.argv[3])

#processing
costo_zapatilla=(numeros_de_zapatillas*precio_de_zapatilla)
verificador=(costo_zapatilla>400)

if(costo_zapatilla>400):
    print("oferta: ud. ha ganado una mochila")
