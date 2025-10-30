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




         














