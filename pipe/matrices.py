def promedio(empleados):
    sexo=input("digite el sexo para el promedio, f o m: ")
    n=len(empleados)
    acu=0
    con=0
    for i in range(0,n):
        if empleados[i][2]==sexo:
             acu=acu+empleados[i][4]
             con=con+1
    if con>0:
        promedio=acu/con
        print("el promedio del sexo, ",sexo," es: ",promedio )
    else:
        print("No se ha ingreado el sexo ",sexo)

def liquidar(empleados,vhora):
    n=len(empleados)
    for i in range(0, n):
        empleados[i][4]=vhora*empleados[i][3]
    return empleados

def valorhora():
    vhora=float(input("Ingrese el valor de la hora: "))
    return vhora

def modificar(empleados):
    cod=int(input("Digite el codigo a modificar: "))
    n=len(empleados)
    for i in range(0, n):
        if empleados[i][0]==cod:
            nombre=input("Ingrese el nombre: ")
            sexo=input("Digite el sexo: ")
            horas=float(input("Digite la cantidad de horas: "))
            empleados[i][1]=nombre
            empleados[i][2]=sexo
            empleados[i][3]=horas
    return empleados

def imprimir(empleados):
    print(empleados)

def crear(cod):
    empleado=[]
    nombre=input("Digite el nombre: ")
    sexo=input("Digite el sexo: ")
    horas=float(input("Digite el horas: "))
    empleado.append(cod)
    empleado.append(nombre)
    empleado.append(sexo)
    empleado.append(horas)
    empleado.append(0.0)  #que es esto
    return empleado
    
def menu():
    opc=0
    cod=2000
    vhora=0
    empleados=[]
    while opc<7:
        print("1. Crear empleado (cod, nombre, sexo, horas)")
        print("2. Imprimir empleados")
        print("3. modificar empleado")
        print("4. ingresar el valor de la hora")
        print("5. Liquidar empleados")
        print("6. promedio segun sexo")
        print("7. Salir")
        opc=int(input("Digite una opcion: "))
        if opc==1:
            empleados.append(crear(cod))
            cod=cod+1
        if opc==2:
            imprimir(empleados)
        if opc==3:
            empleados=modificar(empleados)
        if opc==4:
            vhora=valorhora()
        if opc==5:
            empleados=liquidar(empleados,vhora)
        if opc==6:
            promedio(empleados)
menu()

