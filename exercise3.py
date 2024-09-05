# Ingreso de datos
C = float(input("Introduce el capital inicial: "))
I = float(input("Introduce el interés (entre 0 y 100): "))
M = int(input("Introduce el número de años: "))

# Verificar que los valores sean válidos
if C > 0 and 0 <= I <= 100 and M > 0:
    # Proceso acumulativo para M años
    for j in range(1, M + 1):
        C = C + (C * I / 100)

    # Mostrar resultado final
    print(f"Tienes: {C:.2f} soles")
else:
    print("Error: Los valores ingresados no son válidos.")