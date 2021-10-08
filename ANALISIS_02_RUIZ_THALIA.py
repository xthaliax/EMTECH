import csv 
import os

def menu_principal(): #Impresión del menú y definición de la opción requerida
    m='l'
    while m!='1' and m!='2' and m!='3' and m!='4':
        os.system("cls")
        print("\n\t\t MENÚ PRINCIPAL")
        print("\n\n Ingresa la opción que deseas... ")
        print("\n\t 1.- Rutas de importación y exportación \n\t 2.- Medio de transporte utilizado \n\t 3.- Valor total de importaciones y exportaciones \n\t 4.- Salir del programa")

        m=input("\n\n\t >> ")

    return m

def abrir_archivo(): #Abre el archivo csv y guarda toda la información en una lista
    lector=list()
    x=list()

    with open("synergy_logistics_database.csv","r") as archivo_exp:
        lector=csv.reader(archivo_exp)
        for linea in lector: 
            x.append(linea)
    
    return x

def lista_exportaciones(lista): #Crea la lista de todas las rutas disponibles
    x=list()
    for elemento in lista:
        x.append(elemento[2]+"-"+elemento[3])
    
    x=set(x)
    
    return x

def lista_unicos(lista,columna): #Crea una lista de todos los valores únicos de una columna de la base de datos
    x=list()
    for elemento in lista:
        x.append(elemento[columna])
    
    x=set(x)
    
    return x

def imprimir_conteo(lista,estado): #Imprime las mejores rutas de exportaciones e importaciones
    os.system("cls")
    print(f"\n\t\t 10 MEJORES RUTAS DE {estado.upper()}")
    i=1
    for elemento in lista: 
        print(f"\n\t {i}.- Ruta : {elemento[1]} ")
        print(f"\t {estado} : {elemento[0]}")
        i+=1
        if i==11:
            break


def conteo_rutas(lista,rutas,estado): #Cuenta la cantidad de veces que se ha hecho una ruta 
    x=list()
    for ruta in rutas: 
        suma=0
        for elemento in lista: 
            aux=elemento[2]+"-"+elemento[3]
            if aux==ruta and estado==elemento[1]:
                suma+=1
        if suma==0:
            continue
        else:
            x.append([suma,ruta])
    
    x=reversed(sorted(x))

    if estado=="Exports":
        imprimir_conteo(x,"Exportaciones")
    else:
        imprimir_conteo(x,"Importaciones")


def imprimir_transporte(lista,estado): #Imprime los mejores medios de transporte de exportaciones e importaciones
    print(f"\n\t\t  MEJORES MEDIOS DE TRANSPORTE DE {estado.upper()}")
    i=1
    for elemento in lista: 
        print(f"\n\t {i}.- Medio : {elemento[1]} ")
        print(f"\t {estado} : {elemento[0]}")
        i+=1
        if i==5:
            break


def conteo_transporte(lista,vias,estado): #Cuenta la cantidad de veces que se ha ocupado un medio de transporte
    x=list()
    for via in vias: 
        suma=0
        for elemento in lista: 
            if elemento[7]==via and estado==elemento[1]:
                suma+=1
        if suma==0:
            continue
        else:
            x.append([suma,via])
    
    x=reversed(sorted(x))

    if estado=="Exports":
        imprimir_transporte(x,"Exportaciones")
    else:
        imprimir_transporte(x,"Importaciones")


def imprimir_total(lista,total,estado): #Imprime el valor de las exportaciones e importaciones totales y por cada país
    os.system('cls')
    print(f"\n\t\t TOTAL DE {estado.upper()}")
    i=1
    print("\n\t Total : ",total)
    for elemento in lista: 
        print(f"\n\t {i}.- País : {elemento[1]} ")
        print(f"\t Valor de {estado} : {elemento[0]}")
        print(f"\t Porcentaje de {estado} totales : {format(elemento[2]*100,'.4f')} %")
        i+=1

def conteo_total(lista,paises,estado): #Almacena el valor total de importaciones y exportaciones de manera general y por país
    total=0
    x=list()
    for pais in paises: 
        suma=0
        for elemento in lista: 
            if elemento[2]==pais and estado==elemento[1]:
                suma+=int(elemento[9])

        if suma==0:
            continue
        else:
            x.append([suma,pais])
        
        total+=suma
    
    for y in x:
        y.append(round(y[0]/total,5))
    
    x=reversed(sorted(x))

    if estado=="Exports":
        imprimir_total(x,total,"Exportaciones")
    else:
        imprimir_total(x,total,"Importaciones")


exportaciones=abrir_archivo()
c=lambda x="\n\n\t Cargando ... " : print(x)
w=True

while w==True:

    op1=menu_principal()

    if op1=='1':

        c()
        rutas=lista_exportaciones(exportaciones)
    
        conteo_rutas(exportaciones,rutas,"Exports")
        input("\n\n Presione enter para ver la siguiente lista ... ")
        conteo_rutas(exportaciones,rutas,"Imports")
        input("\n\n Presione enter para regresar al menú ... ")
    
    if op1=='2':

        c()

        transportes=lista_unicos(exportaciones,7)
        os.system("cls")
        conteo_transporte(exportaciones,transportes,"Exports")
        conteo_transporte(exportaciones,transportes,"Imports")
        input("\n\n Presione enter para regresar al menú ... ")
    
    if op1=='3':

        c()
        paises=lista_unicos(exportaciones,2)
        conteo_total(exportaciones,paises,"Exports")
        input("\n\n Presione enter ver la siguiente lista ... ")
        conteo_total(exportaciones,paises,"Imports")
        input("\n\n Presione enter para regresar al menú ... ")

    if op1=='4':
        w=False
