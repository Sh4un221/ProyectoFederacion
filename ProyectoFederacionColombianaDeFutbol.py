import os
os.system('cls')
from tabulate import tabulate
tituloRegistroDeEquipos="""
+++++++++++++++++++++++++++++++++++++++
+   FEDERACION COLOMBIANA DE FUTBOL   +
+++++++++++++++++++++++++++++++++++++++
"""
opciones="1. Registro de equipos\n2. Registro de fecha\n3. Tabla de posiciones\n4. Mostrar reporte\n5. Finalizar el programa"
isActivate=True
informacionPartidos=[]
fechasRegistradas=[]
partidosJugados=0
partidosGanados=0
partidosPerdidos=0
partidosEmpatados=0
golesAnotados=0
golesEnContra=0
totalDePuntos=0
while isActivate:
    os.system('cls')
    print(tituloRegistroDeEquipos)
    print(opciones)    
    op=int(input("):_"))
    if(op==1):
        os.system('cls')
        print(tituloRegistroDeEquipos)
        noExiste=True
        nombreEquipo=str(input("Ingrese el nombre del equipo que va a registrar:_"))
        for i,item in enumerate(informacionPartidos):
            if(item[0]==nombreEquipo):
                noExiste=False
            else:
                i=+1
        if(noExiste):
            if(nombreEquipo!=""):
                informacionPartidos.append([nombreEquipo,partidosJugados,partidosGanados,partidosPerdidos,partidosEmpatados,golesAnotados,golesEnContra,totalDePuntos])
                print("Equipo registrado exitosamente")
                os.system('pause')
            else:
                print("No se ingreso nombre")
                os.system('pause')
            os.system('cls')
        else:
            print("El equipo ",nombreEquipo," ya fue registrado")
            os.system('pause')
    elif(op==2):
        nombreEquipoLocal=str(input("Ingrese el nombre del equipo local: "))
        nombreEquipoVisitante=str(input("Ingrese el nombre del equipo visitante: "))
        golesAnotadosL=int(input("Ingrese numero de goles que anoto el equipo local: "))
        golesAnotadosV=int(input("Ingrese el numero de goles que anoto el equipo visitante: "))
        entra=False
        contCorrecto=int(0)
        for i,item in enumerate(informacionPartidos):
            if((item[0]==nombreEquipoLocal)or(item[0]==nombreEquipoVisitante)):
                contCorrecto+=1
            else:
                i+=1
            if(contCorrecto==2):
                entra=True
            elif(contCorrecto==1):
                print("Uno de los equipos ingresados no se encuentra registrado")
                os.system('pause')    
            elif(contCorrecto==0):
                print("Ninguno de los equipos ingresados estan registrados")    
                os.system('pause')    
        if(entra):
            for i,item in enumerate(informacionPartidos):
                if(nombreEquipoLocal in item):  
                    item[5]+=golesAnotadosL
                    item[6]+=golesAnotadosV
                    item[1]+=1
                    if(golesAnotadosL>golesAnotadosV):
                        item[2]+=1
                        item[7]+=3
                    elif(golesAnotadosL==golesAnotadosV):
                        item[4]+=1
                        item[7]+=1
                    else:
                        item[3]+=1
                    
                if(nombreEquipoVisitante in item):
                    item[5]+=golesAnotadosV
                    item[6]+=golesAnotadosL 
                    item[1]+=1
                    if(golesAnotadosV>golesAnotadosL):
                        item[2]+=1
                        item[7]+=3
                    elif(golesAnotadosV==golesAnotadosL):
                        item[4]+=1
                        item[7]+=1
                    else:
                        item[3]+=1
                i+=1
            fechasRegistradas.append([nombreEquipoLocal,nombreEquipoVisitante,golesAnotadosL,golesAnotadosV])
            if (golesAnotadosL>golesAnotadosV):
                os.system('cls')
                print("El equipo ",nombreEquipoLocal," que estaba jugando de local gano con ",golesAnotadosL," goles")
                print("El equipo ",nombreEquipoVisitante," perdió")
                os.system('pause')
            elif(golesAnotadosL==golesAnotadosV):
                os.system('cls')
                print("El equipo ",nombreEquipoLocal," y el equipo ",nombreEquipoVisitante," empataron")
                os.system('pause')
            else:
                os.system('cls')
                print("El equipo ",nombreEquipoVisitante," que estaba jugando de visitante gano con ",golesAnotadosV," goles")
                print("El equipo ",nombreEquipoLocal," perdió")
                os.system('pause')
    elif(op==3):
        os.system('cls')
        print(tabulate(informacionPartidos,headers=['Equipo','PJ','PG','PP','PE','GF','GC','PT']))
        os.system('pause')
    elif(op==4):
        mayorGoles=int(0)
        mayorPuntos=int(0)
        mayorPartidosGanados=int(0)
        totalGolesTorneo=int(0)
        totalDePartidosJugados=int(0)
        nombreEquipoGF=""
        nombreEquipoMP=""
        nombreEquipoPG=""
        for i,item in enumerate(informacionPartidos):
            if(item[7]>mayorPuntos):
                mayorPuntos=item[7]
                nombreEquipoMP=item[0]
            if(item[5]>mayorGoles):
                mayorGoles=item[5]
                nombreEquipoGF=item[0]
            totalGolesTorneo+=item[5]
            if(item[2]>mayorPartidosGanados):
                mayorPartidosGanados=item[2]
                nombreEquipoPG=item[0]
            totalDePartidosJugados+=item[1]
            i=+1
        print("El equipo con mayor numero de goles es: ",nombreEquipoGF)
        print("El equipo con mayor numero de puntos es: ",nombreEquipoMP)
        print("El equipo con mayor numero de partidos ganados es: ",nombreEquipoPG)
        print("El total de goles que se marcaron en este torneo es: ",totalGolesTorneo)
        print("El porcentaje de goles del torneo por partido jugado fue: ",(totalGolesTorneo/totalDePartidosJugados))
        os.system('pause')
        
    elif(op==5):
        os.system('cls')
        isActivate=False
        print("Gracias por usar el programa\nTenga un buen dia.")
    else:
        os.system('cls')
        print("No ha ingresado ninguna de las opciones, por favor digite las opciones indicadas.")
        os.system('pause')
        os.system('cls')
            
           

                
        
        
        

        

        



