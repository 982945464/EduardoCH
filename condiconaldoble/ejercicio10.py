import os
#declarar variables
examen1,examen2,examen3=0.0,0.0,0.0
promedio=0.0

#input
examen1=int(os.sys.argv[1])
examen2=int(os.sys.argv[2])
examen3=int(os.sys.argv[2])

#processing
promedio_final=round(examen1+examen2+examen3)/3

if(promedio_final>14):
    print("ud aprovo el curso")
else:
    print("ud desaprovo el curso")
