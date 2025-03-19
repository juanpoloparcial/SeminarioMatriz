print("Ejercicio de Matriz. Nombres, notas y Edad")

def ingresar_datos():
    personas = []  # Lista para almacenar los datos de las personas

    while True:
        # Solicitar datos
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        nota = float(input("Ingrese la nota: "))

        # Agregar persona a la lista
        personas.append({"nombre": nombre, "edad": edad, "nota": nota})

        # Preguntar si se desea continuar o finalizar
        continuar = input("¿Desea ingresar otra persona? (si/no): ").lower()
        if continuar != 'si':
            break

    return personas

def mostrar_listado(personas):
    print("\nListado Completo:")
    for persona in personas:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Nota: {persona['nota']}")

def mostrar_listado_ordenado(personas):
    # Ordenar la lista por la nota de mayor a menor
    personas_ordenadas = sorted(personas, key=lambda x: x['nota'], reverse=True)

    print("\nListado Ordenado por Nota (Mayor a Menor):")
    for persona in personas_ordenadas:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Nota: {persona['nota']}")

# Función principal
def main():
    personas = ingresar_datos()  # Ingresar los datos de las personas
    mostrar_listado(personas)  # Mostrar listado completo
    mostrar_listado_ordenado(personas)  # Mostrar listado ordenado por nota

# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
