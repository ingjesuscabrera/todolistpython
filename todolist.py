# Crear un diccionario para almacenar la lista de tareas
lista_de_tareas = {}

# Función para agregar una tarea a la lista
def agregar_tarea():
    # Solicitar al usuario la descripción de la nueva tarea
    tarea = input("Ingrese la nueva tarea: ")

    # Obtener la longitud actual de la lista de tareas y sumar 1 para obtener un número único
    nuevo_id = len(lista_de_tareas) + 1

    # Crear un diccionario que representa la nueva tarea
    nueva_tarea = {"tarea": tarea, "completada": False}

    # Agregar la nueva tarea al diccionario de la lista de tareas
    lista_de_tareas[nuevo_id] = nueva_tarea

    # Imprimir un mensaje de confirmación
    print("Tarea agregada a la lista.")

# Función para marcar una tarea como completada
def marcar_completada():
    # Solicitar al usuario el número de tarea que desea marcar como completada
    tarea_id = int(input("Ingrese el número de tarea que desea marcar como completada: "))

    # Verificar si el número de tarea existe en la lista de tareas
    if tarea_id in lista_de_tareas:
        # Marcar la tarea como completada cambiando el valor a True
        lista_de_tareas[tarea_id]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Tarea no encontrada.")

# Función para mostrar la lista de tareas
def mostrar_lista():
    print("\nLista de Tareas:")
    for tarea_id, tarea_info in lista_de_tareas.items():
        tarea = tarea_info["tarea"]
        completada = tarea_info["completada"]

        # Determinar el estado de la tarea (pendiente o completada)
        estado = "Completada" if completada else "Pendiente"

        # Mostrar el número de tarea, descripción y estado
        print(f"{tarea_id}. {tarea} - {estado}")

# Menú principal
while True:
    print("\nMenú de Tareas:")
    print("1. Agregar Tarea")
    print("2. Marcar Tarea como Completada")
    print("3. Mostrar Lista de Tareas")
    print("4. Salir")

    # Solicitar al usuario que seleccione una opción del menú
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        marcar_completada()
    elif opcion == "3":
        mostrar_lista()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")