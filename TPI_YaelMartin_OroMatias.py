import csv


# -----------------------------
# CARGA CSV
# -----------------------------

def cargar_paises(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("Archivo CSV no encontrado.")

    except Exception as e:
        print("Error al leer CSV:", e)

    return paises


# -----------------------------
# AGREGAR PAIS
# -----------------------------

def agregar_pais(paises):

    nombre = input("Nombre: ").strip().capitalize()
    continente = input("Continente: ").strip().capitalize()

    if nombre == "" or continente == "":
        print("No se permiten campos vacíos.")
        return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("Debe ingresar números.")
        return

    columnas = ["nombre","poblacion","superficie","continente"]

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    with open("paises.csv", "a", newline="", encoding="utf-8") as archivo:
        
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writerow(pais)


    print("País agregado correctamente.")


# -----------------------------
# ACTUALIZAR
# -----------------------------

def actualizar_pais(paises):

    nombre = input("Ingrese país a actualizar: ").strip().capitalize()

    for pais in paises:

        if pais["nombre"].capitalize() == nombre:

            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
            except ValueError:
                print("Dato inválido.")
                return

            print("Actualización exitosa.")
            return

    print("País no encontrado.")


# -----------------------------
# BUSCAR
# -----------------------------

def buscar_pais(paises):

    texto = input("Ingrese nombre a buscar: ").strip().capitalize()

    encontrados = []

    for pais in paises:
        if texto in pais["nombre"].capitalize():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron resultados.")
    else:
        for pais in encontrados:
            print(pais)


# -----------------------------
# FILTRAR CONTINENTE
# -----------------------------

def filtrar_continente(paises):

    continente = input("Continente: ").strip().capitalize()

    encontrados = []

    for pais in paises:

        if pais["continente"].strip().capitalize() == continente:
            encontrados.append(pais)

    for pais in encontrados:
        print(pais)

    if len(encontrados) == 0:
        print("No hay resultados.")


# -----------------------------
# FILTRAR POBLACION
# -----------------------------

def filtrar_poblacion(paises):

    minimo = int(input("Población mínima: "))
    maximo = int(input("Población máxima: "))

    if maximo < minimo:
        print("Error: la población máxima no puede ser menor que la población mínima.")
        return

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:
            print(pais)


# -----------------------------
# FILTRAR SUPERFICIE
# -----------------------------

def filtrar_superficie(paises):

    minimo = int(input("Superficie mínima: "))
    maximo = int(input("Superficie máxima: "))

    if maximo < minimo:
        print("Error: la superficie máxima no puede ser menor que la superficie mínima.")
        return

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:
            print(pais)


# -----------------------------
# ORDENAR
# -----------------------------



def ordenar_nombre(paises):
    
    paises_ordenados=paises.copy() # Utilizamos el metodo .copy() para crear una copia de la lista original y evitar que las modificaciones que hagamos afecten a la lista original.
    
    for i in range(len(paises_ordenados)):
        for j in range(len(paises_ordenados) - 1 - i):
            
            if paises_ordenados[j]["nombre"]>paises_ordenados[j+1]["nombre"]:
                auxiliar = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j+1]
                paises_ordenados[j+1] = auxiliar
    
    for pais in paises_ordenados:
        print(pais)


def ordenar_poblacion(paises):
    
    paises_ordenados=paises.copy() # Utilizamos el metodo .copy() para crear una copia de la lista original y evitar que las modificaciones que hagamos afecten a la lista original.
    
    for i in range(len(paises_ordenados)):
        for j in range(len(paises_ordenados) - 1 - i):
            
            if paises_ordenados[j]["poblacion"]>paises_ordenados[j+1]["poblacion"]:
                auxiliar = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j+1]
                paises_ordenados[j+1] = auxiliar
    
    for pais in paises_ordenados:
        print(pais)
    return paises_ordenados
def ordenar_superficie_ascendente(paises):
    
    paises_ordenados=paises.copy() # Utilizamos el metodo .copy() para crear una copia de la lista original y evitar que las modificaciones que hagamos afecten a la lista original.
    
    for i in range(len(paises_ordenados)):
        for j in range(len(paises_ordenados) - 1 - i):
            
            if paises_ordenados[j]["superficie"]>paises_ordenados[j+1]["superficie"]:
                auxiliar = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j+1]
                paises_ordenados[j+1] = auxiliar
    
    for pais in paises_ordenados:
        print(pais)

def ordenar_superficie_descendente(paises):
    
    paises_ordenados=paises.copy() # Utilizamos el metodo .copy() para crear una copia de la lista original y evitar que las modificaciones que hagamos afecten a la lista original.
    
    for i in range(len(paises_ordenados)):
        for j in range(len(paises_ordenados) - 1 - i):
            
            if paises_ordenados[j]["superficie"]<paises_ordenados[j+1]["superficie"]:
                auxiliar = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j+1]
                paises_ordenados[j+1] = auxiliar
    
    for pais in paises_ordenados:
        print(pais)

# -----------------------------
# ESTADISTICAS
# -----------------------------

def estadisticas(paises):

    mayor_poblacion = ordenar_poblacion(paises)[-1]
    menor_poblacion = ordenar_poblacion(paises)[0]
    sumatoria_poblacion = 0
    sumatoria_superficie = 0
    continentes = {}

    for pais in paises:

        sumatoria_poblacion += pais["poblacion"]
        sumatoria_superficie += pais["superficie"]
        cont = pais["continente"]

        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1


    promedio_poblacion = sumatoria_poblacion / len(paises)
    promedio_superficie = sumatoria_superficie / len(paises)
    



    

    print("\nESTADISTICAS")
    print(f"Mayor población: {mayor_poblacion["nombre"]}")
    print(f"Menor población: {menor_poblacion["nombre"]}")
    print(f"Promedio población: {round(promedio_poblacion, 2)}")
    print(f"Promedio superficie: {round(promedio_superficie, 2)}")

    print("\nPaíses por continente:")

    for k, v in continentes.items():
        print(k, ":", v)


# -----------------------------
# MENU
# -----------------------------

def menu():

    paises = cargar_paises("paises.csv")

    while True:

        print("\n--- MENU ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar por nombre")
        print("8. Ordenar por población")
        print("9. Ordenar por superficie")
        print("10. Estadísticas")
        print("0. Salir")

        opcion = input("Opción: ")
        match opcion:
            case "1":
                agregar_pais(paises)

            case "2":
                actualizar_pais(paises)

            case "3":
                buscar_pais(paises)

            case "4":
                filtrar_continente(paises)

            case "5":
                filtrar_poblacion(paises)

            case "6":
                filtrar_superficie(paises)

            case "7":
                ordenar_nombre(paises)

            case "8":
                ordenar_poblacion(paises)

            case "9":
                descendente = input("1-Ascendente 2-Descendente: ")
                match descendente:
                    case "1":
                        ordenar_superficie_ascendente(paises)
                    case "2":
                        ordenar_superficie_descendente(paises)
                    case _:
                        print("Opción inválida.")

            case "10":
                estadisticas(paises)

            case"0":
                print("Fin del programa.")
                break

            case _:
                print("Opción inválida.")


menu()