# Ingreso de datos
M = int(input("Introduce el número de años (entre 1 y 30): "))
N = int(input("Introduce el número de sucursales (entre 1 y 35): "))

# Verificar si los valores están dentro del rango permitido
if 1 <= M <= 30 and 1 <= N <= 35:
    # Inicializar matriz de ventas
    ventas = []

    # Ingresar los montos de ventas para cada año y sucursal
    for i in range(M):
        fila = []
        print(f"Introduce las ventas del año {i+1}:")
        for j in range(N):
            monto = float(input(f"Sucursal {j+1}: "))
            fila.append(monto)
        ventas.append(fila)

    # a. Calcular el promedio de ventas por año
    promedios_ventas_anuales = []
    for i in range(M):
        promedio = sum(ventas[i]) / N
        promedios_ventas_anuales.append(promedio)
        print(f"Promedio de ventas del año {i+1}: {promedio:.2f}")

    # b. Determinar el año con mayor promedio de ventas
    mayor_promedio = max(promedios_ventas_anuales)
    anio_mayor_promedio = promedios_ventas_anuales.index(mayor_promedio) + 1
    print(f"El año con mayor promedio de ventas es el año {anio_mayor_promedio} con un promedio de {mayor_promedio:.2f}")

else:
    print("Error: El número de años o sucursales no está en el rango permitido.")


#Ejemplo de resultados
#Promedio de ventas del año 1: 5.00
#Promedio de ventas del año 2: 4.80
#El año con mayor promedio de ventas es el año 1 con un promedio de 5.00