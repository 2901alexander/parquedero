def menuprincipal():
    valores_tarifas = [0, 0]  # Inicializamos con 0 las tarifas de automóvil y motocicleta
    while True:
        print("1. Ingresar Tarifas")
        print("2. Mostrar Tarifas")
        print("3. Modificar Tarifas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Entrada no válida. Por favor ingrese un número.")
            continue

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
            print("Opción no válida, intente de nuevo")

def submenuingresarifas(valores_tarifas):
    while True:
        print("1. Ingresar Tarifa de Automóvil")
        print("2. Ingresar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        opcion = input("Digite una opción: ")

        if not opcion.isdigit():
            print("Entrada no válida. Por favor ingrese un número.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            valorminauto = int(input("Ingrese el valor a cobrar por minuto para los automóviles: "))
            valores_tarifas[0] = valorminauto
        elif opcion == 2:
            valorminmoto = int(input("Ingrese el valor a cobrar por minuto para las motocicletas: "))
            valores_tarifas[1] = valorminmoto
        elif opcion == 3:
            break
        else:
            print("Opción no válida, intente de nuevo")

    return valores_tarifas

def mostrartarifas(valores_tarifas):
    print("Tarifas actuales:")
    print(f"Automóviles: {valores_tarifas[0]}")
    print(f"Motocicletas: {valores_tarifas[1]}")

def modificartarifas(valores_tarifas):
    while True:
        print("1. Modificar Tarifa de Automóvil")
        print("2. Modificar Tarifa de Motocicleta")
        print("3. Regresar al subMenú Tarifas")
        opcion = input("Digite una opción: ")

        if not opcion.isdigit():
            print("Entrada no válida. Por favor ingrese un número.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            valorminauto = int(input("Ingrese el nuevo valor a cobrar por minuto para los automóviles: "))
            valores_tarifas[0] = valorminauto
        elif opcion == 2:
            valorminmoto = int(input("Ingrese el nuevo valor a cobrar por minuto para las motocicletas: "))
            valores_tarifas[1] = valorminmoto
        elif opcion == 3:
            break
        else:
            print("Opción no válida, intente de nuevo")

    return valores_tarifas

# Inicia el menú principal
menuprincipal()
