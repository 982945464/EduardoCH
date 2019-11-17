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

if(precio_botella>200):
    print("Ha ganado un vale por 100 soles")
else:
    print("siga intentando")
