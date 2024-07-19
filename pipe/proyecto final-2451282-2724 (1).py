
        
def tarifas():
    opc=0
    while opc<5:
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Regresar al Menú principal")
        opc=int(input("Digite una opcion: "))
        if opc==1:
            submenufarifas()
        if opc==2:
            pass
        if opc==3:
            pass
        if opc==4:

def submenuingretarifas():
    opc=0
    valormin=[]
    while opc<4:
        print("1. Ingresar Tarifa de Automóvil")
        print("2. Ingresar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        opc=int(input("Digite una opcion: "))
        if opc==1:
            valorminauto=int(input("Ingrese el valor a cobrar por minuto para los automoviles: "))
            valormin.insert(0, valorminauto)
        if opc==2:
            valorminmoto=int(input("Ingrese el valor a cobrar por minuto para las motos: "))
            valormin.append(1, valorminmoto)
        if opc==3:
             return valormin

def mostrartarifas(valormin):
    if len(valormin)==2 or len(valormin):
        print("Valor por minuto auto: ",valormin[0])
        print("Valor por minuto moto: ",valormin[1])
    else:
        print("0")

def modificartarifas(valormin):
    opc=0
    while opc<4:
        print("1. Modificar Tarifa Automóvil")
        print("2. Modificar Tarifa Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        opc=int(input("Digite una opcion: "))
        if opc==1:
            modtarifauto()
        if opc==2:
            modtarifamoto
        if opc==3:

def modtarifauto(valormin):
    pass

#-------------------MENU PRINCIPAL (este llama a las demas funciones)--------------    
def menuprincipal():
    opc=0
    while opc<8:
        print("1. Tarifas") 
        print("2. Ingresar vehículo")
        print("3. Buscar vehículo")
        print("4. Mostrar Registros")
        print("5. Salida de vehículo")
        print("6. Buscar Factura")
        print("7. Cuadre de Caja")
        print("8. salir.")
        opc=int(input("Digite una opcion: "))
        if opc==1:
            tarifas()
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
        if opc==7:
            empleados=liquidar(empleados,vhora)