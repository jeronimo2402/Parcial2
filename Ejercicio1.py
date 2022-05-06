
def invertir(arr):
    arr2 = []
    for i in range(cantidad):
        arr2.append(arr[(cantidad-1)-i])

    return arr2

print("Bienvenido al programa que invierte arrays")

arr1 = []

cantidad = int(input("Ingrese la cantidad de elementos que tendrá el array: "))

for i in range(cantidad):
    arr1.append(input(f"Ingrese el valor del elemento {i+1}: "))

arr2 = invertir(arr1)

print(f"El array original es: {arr1}")
print(f"El array invertido es: {arr2}")
