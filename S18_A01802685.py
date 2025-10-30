pares impares
numeros=[22,24,38,40,48]
pares=[]
impares=[]
for n in numeros:
  if n % 2 == 0: 
    pares.append(n)
  else:
    impares.append(n)



temperaturas=[14,16,18,20,22,24, 30, 35]
tempPromedio = sum(temperaturas)/len(temperaturas)

for temp in temperaturas:
    if temp < tempPromedio:
        print(temp, " está debajo del promedio")
    elif temp > tempPromedio:
        print(temp, " está arriba del promedio")





nombres = [“Maya”, “rey”, “mauri”, “nico”, “Juan”]
notas = [88, 70, 35, 80, 60]

promclase = sum(notas) / len(notas)
print(“Promedio grupo:”, prom_clase)

reprobados = []
for i in range(len(nombres)):
    if notas[i] < 70:
        reprobados.append(nombres[i])

print(“Alumnos reprobados:”, reprobados)

aprobados = len(nombres) - len(reprobados)
porcentaje = (aprobados * 100) / len(nombres)
print(“Aprobados:”, porcentaje, “%”)


numeros = [8, 3, 15, 2, 10, 7]
print(“Número mayor:”, max(num))
print(“Número menor:”, min(num))
print(“Ordenados de menor a mayor:”, sorted(num))


usuario = [“maya”, “pato”, “regina”]

nuevo = input(“Pon un nombre“)

while nuevo in users:
    print(“ ese ya esta”)
    nuevo = input(“Escribe un nombre diferente: “)

users.(nuevo)
print(“Usuario agregado:”, nuevo)
print(“Usuarios ahora:”, nombre)








         














