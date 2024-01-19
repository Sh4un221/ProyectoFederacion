# LA FEDERACION COLOMBIANA DE FUTBOL DESEA CREAR UN PROGRAMA QUE LE PERMITA
# LLEVAR EL CONTROL Y REGISTRO DE TODOS LOS EQUIPOS QUE SE ENCUENTRAN
# PARTICIPANDO EN LA LIGA BETPLAY. LA FEDERACION DESEA ORGANIZAR EL TORNEO
# TENIENDO EN CUENTA LA SIGUIENTE INFORMACION:

#     - NOMBRE DEL EQUIPO
#     - PJ
#     - PG
#     - PP
#     - PE
#     - GF
#     - GC
#     - TP

# REQUERIMIENTOS:
# 1. EL PROGRAMA DEBE PERMITIR REGISTRAR CADA UNO DE LOS EQUIPOS QUE VAN A
# PARTICIPAR EN EL TORNEO, TENGA EN CUENTA QUE AL MOMENTO DE REGISTRAR CADA
# EQUIPO LAS VARIABLES DE PJ,PG,PP,PE,GF,GC,TP DEBEN SER 0

# 2. REGISTRO DE FECHA. EL REGISTRO DE FECHAS SE DEBE INGRESAR LOS EQUIPOS
# QUE SE ENFRENTARON. EL PROGRAMA DEBE PERMITIR SELECCIONAR QUE EQUIPO JUGO DE
# LOCAL Y QUE EQUIPO JUGO DE VISITANTE. ADEMAS SE DEBE REGISTRAR EL MARCADOR DE
# CADA UNO DE LOS EQUIPOS. EL PROGRAMA DEBE DETERMINAR CUAL FUE EL EQUIPO
# GANADOR Y CUAL ES EL PERDEDOR Y ASIGNAR LOS VALORES CORRESPONDIENTES EN LA
# TABLA DE POSICIONES. RECUERDE QUE CADA PARTIDO GANADO EQUIVALE A 3 PUNTO
# Y LOS EMPATADOS EQUIVALEN A 1 PUNTO.

# 3. REPORTES
#     A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO
#     B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE
#     C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO
#     D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS
#     E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO
import os
os.system('cls')
tituloRegistroDeEquipos="""
+++++++++++++++++++++++++++++++++++++++
+   FEDERACION COLOMBIANA DE FUTBOL   +
+++++++++++++++++++++++++++++++++++++++
"""
opciones="1. Registro de equipos\n2. Registro de fecha\n3. Tabla de posiciones\n4.Finalizar el programa"
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
        nombreEquipo=str(input("Ingrese el nombre del equipo que va a registrar:_"))
        if(nombreEquipo!=""):
            informacionPartidos.append([nombreEquipo,partidosJugados,partidosGanados,partidosPerdidos,partidosEmpatados,golesAnotados,golesEnContra,totalDePuntos])
        else:
            print("No se ingreso nombre")
            os.system('pause')
        
        os.system('cls')
    elif(op==2):
        nombreEquipoLocal=str(input("Ingrese el nombre del equipo local: "))
        nombreEquipoVisitante=str(input("Ingrese el nombre del equipo visitante: "))
        golesAnotadosL=int(input("Ingrese numero de goles que anoto el equipo local "))
        golesAnotadosV=int(input("Ingrese el numero de goles que anoto el equipo visitante "))
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
                else:
                    item[3]+=1
            fechasRegistradas.append([nombreEquipoLocal,nombreEquipoVisitante,golesAnotadosL,golesAnotadosV])
            i+=1
        if (golesAnotadosL>golesAnotadosV):
            print("El equipo ",nombreEquipoLocal," que estaba jugando de local gano con ",golesAnotadosL," goles")
            print("El equipo ",nombreEquipoVisitante," perdió")
            os.system('pause')
        elif(golesAnotadosL==golesAnotadosV):
            print("El equipo ",nombreEquipoLocal," y el equipo ",nombreEquipoVisitante," empataron")
            os.system('pause')
        else:
            print("El equipo ",nombreEquipoVisitante," que estaba jugando de visitante gano con ",golesAnotadosL," goles")
            print("El equipo ",nombreEquipoLocal," perdió")
            os.system('pause')
    elif(op==3):
        pass
    elif(op==4):
        os.system('cls')
        isActivate=False
        print("Gracias por usar el programa\nTenga un buen dia.")
    else:
        os.system('cls')
        print("No ha ingresado ninguna de las opciones, por favor digite las opciones indicadas.")
        os.system('pause')
        os.system('cls')
            
           

                
        
        
        

        

        



