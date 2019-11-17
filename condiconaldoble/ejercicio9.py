import os
#declarar variables
cliente,numero_de_helados,precio_de_helado="",0.0,0.0
verificador= False

#input
cliente=os.sys.argv[1]
numero_de_helados=int(os.sys.argv[2])
precio_de_helado=float(os.sys.argv[3])

#processing
costo_helado=(numero_de_helados*precio_de_helado)
verificador=(costo_helado>150)

if(costo_helado>150):
    print("donofrio agradece su pedido, vuelva pronto")
else:
    print("se le agradece")
