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

#si_el_estudiante_saca_un_promedio_mayor_que_14_estara_aprovado
#si_el_estudiante_saca_un_promedio_menor_que_14_estara_desaprovado
#si_el_estudiante_saca_un_promedio_igual_que_14_dara_otro_examen

if(promedio_final>14):
    print("ud aprovo el curso")

if(promedio_final<14):
    print("ud desaprovo el curso")

if(promedio_final==14):
    print("ud dara otro examen")
