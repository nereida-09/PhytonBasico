# Loops
mi_lista = {1,2,3,4,5}

for i in mi_lista:
    print("El numero es: ", i)
    
resultado = 0
for i in mi_lista:
    resultado += i

    print(f"El resultado de la suma de mi lista es: {resultado}")

    for i in range(2,9):
        print(i)

mi_lista_2 = {"lunes","martes","miercoles","Jueves","viernes"}
for i in mi_lista_2:
    if i !="lunes":
        print(f"Feliz {i}!")

# while loop
i = 0

while i < 5:
    i += 1
    if i==3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i es ahora el mayor o igual a 5")

count = 0
while count < 3:
    for i in mi_lista_2:
        if i != "lunes":
            print(i)
    count += 1