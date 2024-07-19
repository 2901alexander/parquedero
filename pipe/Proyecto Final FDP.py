#Universidad del Valle - Curso de Fundamentos De Programacion
#Juan Esteban Lozano B.
#13 de Diciembre de 2023


#MENU PRINCIPAL
def menu_principal():
	
	#Variable de la opcion
	opc = 1
	
	#lista de las tarifas
	tarifas = [0,0,0]
	
	#Datos
	datos = []
	
	#Variable del consecutivo de la bici
	cons = 202300

	#Variable de la factura
	fact = 0
	
	while opc > 0 and opc < 8:
		print("===================================================================")
		print("MENU PRINCIPAL")
		print("===================================================================")
		print("1. Tarifas")
		print("2. Ingresar Vehiculo")
		print("3. Buscar Vehiculos")
		print("4. Mostrar Registros")
		print("5. Salida de Vehiculos")
		print("6. Buscar Factura")
		print("7. Cuadre de Caja")
		print("8. Salir")
		opc = int(input("Digite la opcion: "))
		
		if opc == 1:
			tarifas = tarifas_opcion(tarifas)
		if opc == 2:
			n = len(datos)
			cons = cons + 1
			fact = fact + 1
			datos = ingresar_vehiculo(datos,fact,cons)
			if n != len(datos):
				if datos[-1][2] != "b":
					cons = cons - 1
			else:
				fact = fact - 1
                        
		if opc == 3:
			buscar_vehiculos(datos)
		
		if opc == 4:
			mostrar_registros(datos)
		
		if opc == 5:
			datos = salida_vehiculo(datos,tarifas)
		
		if opc == 6:
			buscar_factura(datos)
		
		if opc == 7:
			cuadre_caja(datos)


#===========================================================================
#OPCION 1: Tarifas
def tarifas_opcion(tarifas):
			
	#Variable de la opcion
	opc = 1
	
	while opc > 0 and opc < 4:
		print("===================================================================")
		print("TARIFAS: Sub Menu")
		print("===================================================================")
		print("1. Ingresar Tarifas")
		print("2. Mostar Tarifas")
		print("3. Modificar Tarifas")
		print("4. Volver al Menu Principal")
		opc = int(input("Digite la opcion: "))
			
		if opc == 1:
			tarifas = ingresar_tarifas(tarifas)
		if opc == 2:
			mostrar_tarifas(tarifas)
		if opc == 3:
			modificar_tarifas(tarifas)
	
	if opc < 0 or opc > 4:
		print("Porfavor ingrese una opcion dentro del rango de seleccion")
		tarifas_opcion(tarifas)
		
	return(tarifas)


#Tarifas Opc1
def ingresar_tarifas(tarifas):
		
	#Variable de la opcion
	opc = 1
		
	while opc > 0 and opc < 4:
		print("===================================================================")
		print("INGRESAR TARIFAS: Sub Menu")
		print("===================================================================")
		print("1. Ingresar Tarifa de Automóvil")
		print("2. Ingresar Tarifa de Motocicleta")
		print("3. Ingresar Tarifa de Bicicleta")
		print("4. Regresar al sub Menú Tarifas")
		opc = int(input("Digite la opcion: "))
		
		if opc == 1:
			auto_t = int(input("Ingresa el valor a cobrar por minuto para automóviles: "))
			tarifas[0] = auto_t
		
		if opc == 2:
			moto_t = int(input("Ingresa el valor a cobrar por minuto para motocicletas: "))
			tarifas[1] = moto_t
		
		if opc == 3:
			bici_t = int(input("Ingresa el valor a cobrar por minuto para bicicletas: "))
			tarifas[2] = bici_t
	if opc < 0 or opc > 4:
		print("Porfavor ingrese una opcion dentro del rango de seleccion")
		
	return(tarifas)


#Tarifas Opc2
def mostrar_tarifas(tarifas):
	print("Valor por minuto Auto: ",tarifas[0])
	print("Valor por minuto Moto",tarifas[1])
	print("Valor por minuto Bicicleta",tarifas[2])


#Tarifas Opc3
def modificar_tarifas(tarifas):
	
	opc = 1
	
	if tarifas[0] != 0 or tarifas[1] != 0 or tarifas[2] != 0:
		while opc > 0 and opc < 4:
			print("===================================================================")
			print("MODIFICAR TARIFAS: Sub Menu")
			print("===================================================================")
			print("1. Ingresar Tarifa de Automóvil")
			print("2. Ingresar Tarifa de Motocicleta")
			print("3. Ingresar Tarifa de Bicicleta")
			print("4. Regresar al sub Menú Tarifas")
			opc = int(input("Digite la opcion: "))
			
			if opc == 1:
				auto_t = int(input("Digite el valor de la tarifa del automovil: "))
				if auto_t != tarifas[0]:
					tarifas[0] = auto_t
				else:
					print("NO puedes ingresar el mismo valor de antes")
					modificar_tarifas(tarifas)
					
			if opc == 2:
				moto_t = int(input("Digite el valor de la tarifa de la motocicleta: "))
				if moto_t != tarifas[1]:
					tarifas[1] = moto_t
				else:
					print("NO puedes ingresar el mismo valor de antes")
					modificar_tarifas(tarifas)
			
			if opc == 3:
				bici_t = int(input("Digite el valor de la tarifa del automovil: "))
				if bici_t != tarifas[3]:
					tarifas[3] = bici_t
				else:
					print("NO puedes ingresar el mismo valor de antes")
					modificar_tarifas(tarifas)
			
	else:
		print("Aun NO se han ingresado valores para modificar")
	
	return(tarifas)


#===========================================================================
#OPCION 2: Ingresar Vehiculo

def ingresar_vehiculo(datos,fact,cons):
	print("===================================================================")
	print("INGRESAR VEHICULO")
	print("===================================================================")

	v_bici = True
		
	#Validacion de que el vehiculo no esta registrado
	v = True
		
	#validacion
	placa_v = True
		
	#Inicializacion de la fila
	fila = []
		
	#Inicializacion de la placa
	placa = ""
		
	#aviso para el usuario
	print("Para ingresar el vehiculo, digite la siguiente informacion:")
		
	#ingresar tipo de vehiculo
	tipo_v = input("Ingrese el tipo de vehiculo: a: automoviles, m: motocicletas, b: bicicletas: ")
		
	#En caso de ingresar una letra NO correspondiente a ningun vehiculo
	if tipo_v == "a" or tipo_v == "m" or tipo_v == "b":
		#Condicionales para autos y motos
		if tipo_v == "a":
			placa = input("Digite los caracteres de la placa: tres letras seguidas de tres números: ")
				
			if len(placa) != 6:
				placa_v = False
					
			if len(datos) != 0:
				for i in range(0,len(datos)):
					if datos[i][2] == "a" and datos[i][1] == placa:
						v = False
						if datos[i][4] != 0:
							v = True
	
		if tipo_v == "m":
			placa = input("Digite los caracteres de la placa: tres letras seguida de dos números, seguida de una letra: ")
				
			if len(placa) != 6:
				placa_v == False
				
			if len(datos) != 0:
				for i in range(0,len(datos)):
					if datos[i][2] == "m" and datos[i][1] == placa:
						v = False

		if tipo_v == "b":
			con = 0
			for i in range(0,len(datos)):
				if datos[i][2] == "b" and datos[i][4] != 0:
					con += 1
					if con == 5:
						v_bici = False
						print("No quedan espacios para las bicicletas")
                                                
		if v == True and placa_v == True and v_bici == True:
			#Digitar la hora de ingreso
			ingreso_h = int(input("Digite la Hora de ingreso(Formato: hhmm): "))
				
			hh = ingreso_h//100
			mm = ingreso_h%100
				
			#En caso de que se digite una hora invalida
			if hh >= 0 and hh < 24 and mm >= 0 and mm < 60:
				#ingresar nombre del cliente
				nombre = input("Ingrese el Nombre del cliente: ")
					
				#En caso de haber ingresdo un bici, mostrar el consecutivo
				if tipo_v == "b":
					placa = cons
					print("El numero consecutivo de la bicicleta es: ",cons)
						
				#Incluir datos a la lista
				fila.append(fact)
				fila.append(placa)
				fila.append(tipo_v)
				fila.append(nombre)
				fila.append(0)
				fila.append(ingreso_h)
				datos.append(fila)
			else:
				print("Hora no Valida")
		else:
			if placa_v == False:
				print("Placa Invalida")
					
			if v == False:
				print("Vehiculo Ya Registrado")
	else:
		print("Porfavor ingrese una letra correspondiente al vehiculo")
	return datos

#===========================================================================
#OPCION 3: Buscar Vehiculos
def buscar_vehiculos(datos):
	print("===================================================================")
	print("BUSCAR VEHICULO")
	print("===================================================================")
		
	opc = 1
	while opc > 0 and opc < 4:
		print("1. Buscar por Placa")
		print("2. Buscar por Propietario")
		print("3. Regresar al Menu Principal")
		opc = int(input("Digite la opcion: "))
			
		#Buscar por placa
		if opc == 1:
			placa = input("Digite la Placa: ")
			for i in range(0,len(datos)):
				if datos[i][1] == placa and datos[i][4] == 0:
					print(datos[i])
					
		#Buscar por Propietario
		if opc == 2:
			propietario = input("Digite el Propietario: ")
			for i in range(0,len(datos)):
				if datos[i][3] == propietario and datos[i][4] == 0:
					print(datos[i])
					
		#En caso de ingresar una opcion no valida
		if opc < 0 or opc > 4:
			print("Porfavor ingrese una opcion dentro del rango de seleccion")


#===========================================================================
#OPCION 4: Mostrar Registros
def mostrar_registros(datos):
	print("===================================================================")
	print("MOSTRAR REGISTROS")
	print("===================================================================")
		
	opc = 1
		
	while opc > 0 and opc < 4:
		print("1. Mostrar todos los registros")
		print("2. Mostrar solo los registros activos")
		print("3. Regresar al Menu Principal")
		opc = int(input("Digite la opcion: "))
			
		if opc == 1:
			for i in range(0,len(datos)):
				print(datos[i])
					
		if opc == 2:
			for i in range(0,len(datos)):
				if datos[i][4] == 0:
					print(datos[i])
					
		if opc < 0 or opc > 4:
			print("Porfavor ingrese una opcion dentro del rango de seleccion")
			

#===========================================================================
#OPCION 5: Salida de Vehiculo
def salida_vehiculo(datos,tarifas):
	print("===================================================================")
	print("SALIDA DE VEHICULO")
	print("===================================================================")
		
	#Buscar vehiculo por placa o por propietario
	opc = 1
	#Iniciacion de los minutos
	m = 0
		
	while opc > 0 and opc < 3:
		print("1. Buscar por Placa")
		print("2. Buscar por Propietario")
		print("3. Regresar al Menu Principal")
		opc = int(input("Digite la opcion: "))
			
		#Buscar por placa
		if opc == 1:
			placa = input("Digite la Placa: ")
			for i in range(0,len(datos)):
				if datos[i][1] == placa and datos[i][4] == 0:
					#Ingreso de la hora de salida
					salida_h = int(input("Digite la Hora de salida(Formato: hhmm): "))
						
					#Separar la hora y los minutos
					shh = salida_h//100
					smm = salida_h%100
						
					#Hora de ingreso
					ih = datos[i][5]//100
					im = datos[i][5]%100
						
					#Minutos a cobrar
					m = ((shh-ih)*60) + (smm - im)
						
					#Impresion de los valores a cobrar
					if datos[i][2] == "a":
						valor = m*tarifas[0]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[0])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
							
					if datos[i][2] == "m":
						valor = m*tarifas[1]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[1])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
						
					if datos[i][2] == "b":
						valor = m*tarifas[2]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[2])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
		
		#Buscar por Propietario
		if opc == 2:
			propietario = input("Digite el Propietario: ")
			for i in range(0,len(datos)):
				if datos[i][3] == propietario and datos[i][4] == 0:
					#Ingreso de la hora de salida
					salida_h = int(input("Digite la Hora de salida(Formato: hhmm): "))
						
					#Separar la hora y los minutos
					shh = salida_h//100
					smm = salida_h%100
						
					#Hora de ingreso
					ih = datos[i][5]//100
					im = datos[i][5]%100
						
					#Minutos a cobrar
					m = ((shh-ih)*60) + (smm - im)
						
					#Impresion de los valores a cobrar
					if datos[i][2] == "a":
						valor = m*tarifas[0]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[0])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
							
					if datos[i][2] == "m":
						valor = m*tarifas[1]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[1])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
							
					if datos[i][2] == "b":
						valor = m*tarifas[2]
						print("Factura No. ",datos[i][0])
						print("Tarifa por minuto: ",tarifas[2])
						print("Tiempo consumido en minutos: ",m)
						print("Total a Pagar: ",valor)
						datos[i][4] = valor
		
		#En caso de ingresar una opcion no valida
		if opc < 0 or opc > 4:
			print("Porfavor ingrese una opcion dentro del rango de seleccion")
	return datos
			

#===========================================================================
#OPCION 6: Buscar Factura
def buscar_factura(datos):
	print("===================================================================")
	print("BUSCAR FACTURA")
	print("===================================================================")
		
	#Validacion del numero de la factura
	fact = int(input("Ingrese el numero de la Factura: "))
		
	if len(datos) != 0:
		for i in range(0,len(datos)):
			if datos[i][0] == fact:
				print(datos[i])
			
	else:
		print("NO existen Facturas registradas")


#===========================================================================
#OPCION 7: Cuadre de Caja
def cuadre_caja(datos):
	print("===================================================================")
	print("CUADRE DE CAJA")
	print("===================================================================")
		
	#inicializacion de los contadores de vehiculos
	aut = 0
	mot = 0
	bic = 0
	valor_aut = 0
	valor_mot = 0
	valor_bic = 0
	#verificacion de que hay vehiculos
	v = False
	if len(datos) != 0:
		for i in range(0,len(datos)):
			if datos[i][4] != 0:
				v = True
		if v == True:
			for i in range(0,len(datos)):
				if datos[i][4] != 0:
					if datos[i][2] == "a":
						aut += 1
						valor_aut += datos[i][4]
						
					if datos[i][2] == "m":
						mot += 1
						valor_mot += datos[i][4]
						
					if datos[i][2] == "b":
						bic += 1
						valor_bic += datos[i][4]
						
		else:
			print("No hay registros cerrados aun")
			
	else:
		print("No hay registros cerrados aun")
	
	#Impresion de los valores de cuadratura de caja
	print("Total de Autos",aut,"-","Dinero recolectado: ",valor_aut)
	print("Total de Motos",mot,"-","Dinero recolectado: ",valor_mot)
	print("Total de Bicicletas",bic,"-","Dinero recolectado: ",valor_bic)
	return

#===========================================================================
#OPCION 8: Salir
def salir():
	print("===================================================================")
	print("Gracias por utilizar este programa")
	print("===================================================================")
	return

menu_principal()
