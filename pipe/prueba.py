from datetime import datetime
import re
#Universidad del valle 
#Andres Felipe Castaño Valencia
#Codigo: 2451282-2724
#Fundamentos de programacion imperativa
#------------------------------------INICIO CUADRE DE CAJA  PUNTO 7----------------------------------------
def CuadreCaja(ingrVhic):
    aut = 0                                                    #crea variable para bicicleta y para total bicicleta
    mot = 0
    total_aut = 0
    total_mot = 0
    # Verificación de que hay vehiculos
    if len(ingrVhic) != 0:
        for i in range(len(ingrVhic)):
            if ingrVhic[i][4] != 0:
                if ingrVhic[i][2] == "a":                   #repite if o corre el de moto y deja elif para bicicleta y repite el codigo elif ingrVhic[i][2] == "b":
                    if ingrVhic[i][4]!="":
                        aut += 1
                        total_aut += ingrVhic[i][7]
                elif ingrVhic[i][2] == "m":
                    if ingrVhic[i][4]!="":
                        mot += 1
                        total_mot += ingrVhic[i][7]
    else:
        print("No hay vehiculos registrados.")

    # Impresión de los valores de cuadratura de caja                                            # crea print para bicicleta
    print("Total de Autos", aut, "-", "Total sumatoria de plata de autos: ", total_aut)
    print("Total de Motos", mot, "-", "Total sumatoria de plata de motos: ", total_mot)

#------------------------------------FIN CUADRE DE CAJA  PUNTO 7-------------------------------------------
#------------------------------------INICIO BUSCAR FACTURA  PUNTO 6----------------------------------------
def BuscarFactura(ingrVhic):
    
    NumFactura = int(input("Digite numero de factura: "))
    print(NumFactura)
    found = False
    for vehiculo in ingrVhic:
        if vehiculo[0] == NumFactura:  # Asegúrate de que el índice y la condición sean correctos
            print(f"""
            VEHÍCULO ENCONTRADO
            Factura No: {vehiculo[0]}
            Placa: {vehiculo[1]}
            Vehículo tipo: {'Moto' if vehiculo[2] == 'm' else 'Automóvil'}         
            Hora de ingreso: {vehiculo[3]}
            Hora de salida: {vehiculo[4]}
            Nombre: {vehiculo[5]}
            Numero minutos: {vehiculo[6]}
            Total: {vehiculo[7]}
            """)                                                     #modifica esta linea Vehículo tipo: {'Moto' if vehiculo[2] == 'm' 'Automóvil' if vehiculo[2] == 'a' else 'bicicleta'}
            found = True
    if not found:
        print("Factura no encontrada.")
    
#-------------------------------------FIN BUSCAR FACTURA  PUNTO 6------------------------------------------
#------------------------------------INICIO SALIDA DE VEICULOS  PUNTO 5----------------------------------------
def SalidaVehiculos(ingrVhic, valores_tarifas):
    tVehiculo = input("Tipo de vehiculo: ")
    placa = input("Ingrese placa: ")
    horSalida = input("Ingrese hora de salida (HH:MM): ")
    try:
        horSalida_dt = datetime.strptime(horSalida, "%H:%M")
    except ValueError:
        print("Formato de hora de salida incorrecto. Use HH:MM.")
        return
    
    vehiculo_registrado = False
    for vehiculo in ingrVhic:
        if len(vehiculo) < 5:
            print(f"Formato incorrecto de datos del vehículo: {vehiculo}")
            continue

        if tVehiculo == vehiculo[2] and placa == vehiculo[1]:
            vehiculo_registrado = True
            try:
                horaEntr = datetime.strptime(vehiculo[3], "%H:%M")
            except (ValueError, IndexError):
                print("Hora de ingreso incorrecta o no registrada.")
                return
            
            if horSalida_dt < horaEntr:
                print("Hora de salida no puede ser menor que hora de ingreso.")
                return
            
            vehiculo[4] = horSalida  # hora de salida
            
            # Calcular la diferencia entre las horas
            diferencia = horSalida_dt - horaEntr
            
            # Convertir la diferencia a minutos
            diferencia_minutos = diferencia.total_seconds() / 60
            vehiculo[6] = diferencia_minutos  # número de minutos
            
            # Asignar tarifa según tipo de vehículo                                                agrega un if if tVehiculo == 'b': o para moto y deja el elif para bicicleta
            if tVehiculo == 'a':
                vehiculo[7] = diferencia_minutos * valores_tarifas[0]  # total minutos x tarifa automóvil
            elif tVehiculo == 'm':
                vehiculo[7] = diferencia_minutos * valores_tarifas[1]  # total minutos x tarifa motocicleta
            else:
                print(f"Tipo de vehículo '{tVehiculo}' no reconocido.")
                return
            
            print("Registro actualizado.")
            print(f"""
                        Factura No: {vehiculo[0]}
                        Placa: {vehiculo[1]}
                        Vehículo tipo: {'Moto' if vehiculo[2] == 'm' else 'Automóvil'}
                        Hora de ingreso: {vehiculo[3]}
                        Hora de salida: {vehiculo[4]}
                        Nombre: {vehiculo[5]}
                        Numero minutos: {vehiculo[6]}
                        Total: {vehiculo[7]}
                        """)
            break
        
    
    if not vehiculo_registrado:
        print("Vehículo no registrado")
  
#------------------------------------FIN SALIDA DE VEICULOS  PUNTO 5----------------------------------------
#------------------------------------INICIO MOSTRAR REGISTRO DE VEHICULOS  PUNTO 4----------------------------------------
def MostrarRegistros(ingrVhic):
    print(ingrVhic)
    opc=0
    #ENCABEZADO
    titulosAccionesVehiculo= ["FACTURA", "PLACA", "INGRESO", "SALIDA", "MINUTOS", "TOTAL"]

    while opc < 4:
        print("1. Mostrar todos los automóviles")                #crea opcion print ( mostrar bicicleta)
        print("2. Mostrar todas las motocicletas")
        print("3. Regresar al menú principal")
        print("---------------")
        try:
            opc = int(input("Digite una opcion: "))
            if opc == 1:
                print("Tipo de búsqueda: AUTOMÓVILES")                 #repite codigo para if opc == bicicleta: para bicicleta
                print("VEHÍCULO ENCONTRADO")
                print("{:<8} {:<8} {:<10} {:<10} {:<8} {:<8}".format(*titulosAccionesVehiculo))
                #--- :<8 = dice que el primer elemento de la lista lo alinie a la izquierda y que lo separe 8 espacios
                for vehiculo in ingrVhic:
                    
                    
                    if vehiculo[2] == "a":  # Automóvil
                        print("{:<8} {:<8} {:<10} {:<10} {:<8} {:<8}".format(vehiculo[0], vehiculo[1], vehiculo[3], vehiculo[4], vehiculo[6], vehiculo[7]))
                       
            elif opc == 2:
                print("Tipo de búsqueda: AUTOMÓVILES")
                print("VEHÍCULO ENCONTRADO")
                print("{:<8} {:<8} {:<10} {:<10} {:<8} {:<8}".format(*titulosAccionesVehiculo))
                for vehiculo in ingrVhic:
                    if vehiculo[2] == "m":  # Motocicleta
                        print("{:<8} {:<8} {:<10} {:<10} {:<8} {:<8}".format(vehiculo[0], vehiculo[1], vehiculo[3], vehiculo[4], vehiculo[6], vehiculo[7]))
                      
            elif opc == 3:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

#-------------------------------------FIN MOSTRAR REGISTRO DE VEICULOS  PUNTO 4------------------------------------------
#----------------------------------------INICIO BUSQUEDA DE VEICULO  PUNTO 3---------------------------------------------
def BuscarVehiculo(ingrVhic):
    opcBuscarVehiculo = 0
    while opcBuscarVehiculo != 3:  # Cambiado para continuar el menú hasta elegir regresar
        print("1. Buscar motos.")
        print("2. Buscar automóviles.")                                  #crea opcion buscar bicicleta
        print("3. Regresar al menú principal.")                          #repite desde if opcBuscarVehiculo == bicicleta: con datos bicicleta
        try:
            opcBuscarVehiculo = int(input("Digite una opción: "))
            if opcBuscarVehiculo == 1:
                placa = input("Digite la Placa: ")
                found = False
                for vehiculo in ingrVhic:
                    if vehiculo[1] == placa and vehiculo[2] == "m":  # Asegúrate de que el índice y la condición sean correctos
                        print(f"""
                        VEHÍCULO ENCONTRADO
                        Factura No: {vehiculo[0]}
                        Placa: {vehiculo[1]}
                        Vehículo tipo: {'Moto' if vehiculo[2] == 'm' else 'Automóvil'}
                        Hora de ingreso: {vehiculo[3]}
                        Hora de salida: {vehiculo[4]}
                        Nombre: {vehiculo[5]}
                        Numero minutos: {vehiculo[6]}
                        Total: {vehiculo[7]}
                        """)
                        found = True
                if not found:
                    print("Moto no encontrada.")

            elif opcBuscarVehiculo == 2:
                placa = input("Digite la Placa: ")
                found = False
                for vehiculo in ingrVhic:
                    if vehiculo[1] == placa and vehiculo[2] == "a":
                        print(f"""
                        VEHÍCULO ENCONTRADO
                        Factura No: {vehiculo[0]}
                        Placa: {vehiculo[1]}
                        Vehículo tipo: {'Moto' if vehiculo[2] == 'm' else 'Automóvil'}
                        Hora de ingreso: {vehiculo[3]}
                        Hora de salida: {vehiculo[4]}
                        Nombre: {vehiculo[5]}
                        Numero minutos: {vehiculo[6]}
                        Total: {vehiculo[7]}
                        """)
                        found = True
                if not found:
                    print("Automóvil no encontrado.")
            
            elif opcBuscarVehiculo == 3:
                print("Regresando al menú principal.")
            
            else:
                print("Por favor ingrese una opción dentro del rango de selección (1-3).")
        
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")
#------------
#---------------------------------FIN BUSQUEDA DE VEHICULO DE VEICULO  PUNTO 3-------------------------------------------
#-----------------------------------------INGRESO DE VEICULO  PUNTO 2---------------------------------------------
# Definir una función para capturar la información del vehículo

def capturar_informacion(regist):
    vehiculosregist = []
    vehiculosregist.append(regist)
    
    # Expresión regular para validar el formato de la placa de automóvil (3 letras seguidas de 3 números)
    regex_auto = r'^[A-Za-z]{3}\d{3}$'
    # Expresión regular para validar el formato de la placa de moto (3 letras seguidas de 2 números y una letra)
    regex_moto = r'^[A-Za-z]{3}\d{2}[A-Za-z]$'
    
    while True:                                                         #crea una validacion para la placa de bicicleta regex_bicicleta = r'^[A-Za-z]{3}\d{2}[A-Za-z]$'
        placa = input("Número de la placa: ")                           #arregla la exprecion regular
        # Validar el formato de la placa y su unicidad
        if re.match(regex_auto, placa) or re.match(regex_moto, placa):       #crea otro or re.match(regex_bicicleta, placa)
            if placa in vehiculosregist:
                print("La placa ya está registrada")
            else:
                vehiculosregist.append(placa)
                break
        else:
            print("El formato de la placa es incorrecto")
                
    while True:
        tipo_vehiculo = input("Tipo de vehículo (a: automóvil, m: moto): ")                    #ingrsa (b: bicicleta)
        if tipo_vehiculo in ['a', 'm']:                                                           #ingresa en la lista opcion b  ['a', 'm', 'b']
            if (tipo_vehiculo == 'a' and re.match(regex_auto, placa)) or (tipo_vehiculo == 'm' and re.match(regex_moto, placa)):           #valida bicicleta
                vehiculosregist.append(tipo_vehiculo)
                if tipo_vehiculo == 'a':
                    print("Registro de automóvil exitoso.")                 #crea otro if  para bicicleta if tipo_vehiculo == 'b' o para moto y deja el else para bicicleta
                else:
                    print("Registro de motocicleta exitoso.")
                break
            else:
                print("El formato de la placa no corresponde al tipo de vehículo. Ingreselo de nuevo.")
        else:
            print("Tipo de vehículo no válido.")
        
    while True:
        horaIngreso = input("Ingrese la hora inicial hora:minutos (Ej: 03:17): ")
        try:
            horaIn = datetime.strptime(horaIngreso, "%H:%M")
            # Convertir las horas ingresadas en objetos datetime
            horaInic = horaIn.strftime("%H:%M")
            vehiculosregist.append(horaInic)
            break
        except ValueError:
            print("Hora no válida. Por favor, ingrésela en el formato HH:MM.")
    
    vehiculosregist.append("") #hora salida
    
    nombre_cliente = input("Nombre del cliente: ")
    vehiculosregist.append(nombre_cliente)
    vehiculosregist.append(0)
    #vehiculosregist.append(0)
    
    return vehiculosregist


#---------------------------------------FIN INGRESO DE VEICULO  PUNTO 2---------------------------------------------

#-------------------- INICIO OPCION TARIFAS  PUNTO 1---------------------------------------------
def tarifas(valores_tarifas):
    opcion = 0
      # Inicializamos con 0 las tarifas de automóvil y motocicleta
    while opcion < 5:
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Salir") 
        print("---------------")
        opcion = input("Seleccione una opción: ")
        
        try:
            opcion = int(opcion) 

            if opcion == 1:
                valores_tarifas = submenuingresarifas(valores_tarifas)
            elif opcion == 2:
                mostrartarifas(valores_tarifas)
            elif opcion == 3:
                valores_tarifas = modificartarifas(valores_tarifas)
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor ingrese un número entre 1 y 4.")
        except ValueError:  # Maneja el caso en que la entrada no sea un número
                print("Entrada no válida. Por favor ingrese un número.")
    return valores_tarifas        
                

def submenuingresarifas(valores_tarifas):
    opcion = 0
    while opcion < 4:
        print("1. Ingresar Tarifa de Automóvil")             #print(Ingresar tarifa bicicleta)
        print("2. Ingresar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")               #repite una opcion osea opcion == 3 elif opcion == 3: 
        print("---------------")                              #if valores_tarifas[2] == 0:  este seria el tercer elemento de la lista valores tarifa
        opcion = input("Digite una opción: ")

        try:
            opcion = int(opcion)

            if opcion == 1:
                if valores_tarifas[0] == 0:
                    valorminauto = int(input("Ingrese el valor a cobrar por minuto para los automóviles: "))
                    valores_tarifas[0] = valorminauto
                else:
                    print("ya existe un valor")    
            elif opcion == 2:
                if valores_tarifas[1] == 0:
                    valorminmoto = int(input("Ingrese el valor a cobrar por minuto para las motocicletas: "))
                    valores_tarifas[1] = valorminmoto
                else:
                    print("ya existe un valor")
            elif opcion == 3:
                break
            else:
                print("Opción no válida. Por favor ingrese un número entre 1 y 4.")
        except ValueError:  # Maneja el caso en que la entrada no sea un número
                print("Entrada no válida. Por favor ingrese un número.")

    return valores_tarifas

def mostrartarifas(valores_tarifas):
    print("Tarifas actuales:")
    print(f"Valor por minuto Automóviles: {valores_tarifas[0]}")                 #hace un print para mostrar valores_tarifas[2] de bicicleta
    print(f"Valor por minuto Motocicletas: {valores_tarifas[1]}")

def modificartarifas(valores_tarifas):
    opcion = 0
    while opcion < 4:
        print("1. Modificar Tarifa de Automóvil")                  #crea un print() para opcion print("2. Modificar Tarifa de bicicleta")
        print("2. Modificar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        print("---------------")
        opcion = input("Digite una opción: ")

        try:
            opcion = int(opcion)                                  #crea una opcion para bicicleta pero con valores_tarifas[2] = valorminbicicleta
                                                                    
            if opcion == 1:
                valorminauto = int(input("Ingrese el nuevo valor a cobrar por minuto para los automóviles: "))
                valores_tarifas[0] = valorminauto
            elif opcion == 2:
                valorminmoto = int(input("Ingrese el nuevo valor a cobrar por minuto para las motocicletas: "))
                valores_tarifas[1] = valorminmoto
            elif opcion == 3:
                break
            else:
                print("Opción no válida. Por favor ingrese un número entre 1 y 3.")
        except ValueError:  # Maneja el caso en que la entrada no sea un número
                print("Entrada no válida. Por favor ingrese un número.")

    return valores_tarifas

#-------------------------------------------FIN OPCION TARIFAS---------------------------------------------

#-------------------------------------------MENU PRINCIPAL------------------------------------------------
def menuprincipal():
    opc=0
    ingrVhic = []
    valores_tarifas=[0, 0]                 #agrega otro eelemento en cero a valores_tarifas=[0, 0, 0] que son los tres vehiculos 
    regist = 0
    while opc <= 8:
        print("1. Tarifas") 
        print("2. Ingresar vehículo")
        print("3. Buscar vehículo")
        print("4. Mostrar Registros")
        print("5. Salida de vehículo")
        print("6. Buscar Factura")
        print("7. Cuadre de Caja")
        print("8. salir.")
        print("---------------")
        opcion=input("Digite una opcion: ")
        try:
            opc = int(opcion)  # Intenta convertir la entrada a un número entero
            if 1 <= opc <= 8:  # Verifica si está dentro del rango válido
                    if opc==1:
                        tarifas(valores_tarifas)
                    if opc==2:
                        ingrVhic.append(capturar_informacion(regist))
                        regist=regist+1
                    if opc==3:
                        BuscarVehiculo(ingrVhic)
                    if opc==4:
                        MostrarRegistros(ingrVhic)
                    if opc==5:
                        SalidaVehiculos(ingrVhic, valores_tarifas)
                    if opc==6:
                        BuscarFactura(ingrVhic)
                    if opc==7:
                        CuadreCaja(ingrVhic)
                    if opc==8:
                        break
            else:
                print("Opción no válida. Por favor ingrese un número entre 1 y 8.")
        except ValueError:  # Maneja el caso en que la entrada no sea un número
                print("Entrada no válida. Por favor ingrese un número.")
    return ingrVhic
        #else:
            #print("Opción no válida. Por favor ingrese un número entre 1 y 8.")  
        #------BREAK (se usa para detener el bucle despues de ejecutar una opcion)---- 
         

menuprincipal()            