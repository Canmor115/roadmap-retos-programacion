# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
#### Dificultad: Fácil | Publicación: 02/01/24

## --------------------------
## TIPOS DE OPERADORES PYTHON
## --------------------------
# ARITMÉTICOS
# +, -, *, /, %, **
print(f"Suma: 10 + 3 = {10+3}")
print(f"Resta: 10 - 3 = {10-3}")
print(f"Multiplicación: 10 * 3 = {10*3}")
print(f"División: 10 / 3 = {10/3}")
print(f"Módulo (el resto de la división): 10 % 3 = {10%3}")
print(f"Exponencial: 10^3 = {10**3}")
print(f"División entera: 10//3 = {10//3}")

# LÓGICOS
# and
print(f"AND &&: 10+3 = 13 and 5-1 = 4 es {10 + 3 == 13 and 5 - 1 == 4}")
# or
print(f"OR ||: 10+3 = 13 or 5-1 = 4 es {10 + 3 == 13 or 5 - 1 == 4}")
# not
print(f"NOT !: 10+3 = 14 es {not 10 + 3 == 14}")

# DE COMPARACIÓN
# == Igualdad
print(f"¿Igual 5 == 5? {5==5}")
print(f"¿Igual 10 == 5? {10==5}")

# != Diferente
print(f"¿Es diferente 5 != 5? {5!=5}")
print(f"¿Es diferente 10 != 5? {10!=5}")

# > >=
print(f"¿Es mayor: 5 > 5? {5>5}")
print(f"¿Es mayor o igual que: 10 >= 5? {10>=5}")

# < <=
print(f"¿Es mayor: 5 < 5? {5<5}")
print(f"¿Es mayor o igual que: 10 <= 5? {10<=5}")


# ASIGNACIÓN
# Asigna un valor: =
x = 5
print(f"Asignamos 5 al valor de x: x={x}")
# Suma y asigna: +=
x += 2
print(f"Sumamos y asignamos 2 al valor de x: x={x}")
# Resta y asigna: -=
x -= 3
print(f"Restamos y asignamos 3 al valor de x: x={x}")
# Multiplica y asigna: *=
x *= 3
print(f"Multiplicamos el valor de x por 3 y asignamos: x={x}")
# Divide y asigna: /=
x /= 3
print(f"Dividimos el valor de x entre 3 y asignamos: x={x}")
# División entera y asignación: //=
x //= 2
print(f"Dividimos el valor de x entre 3 y asignamos el valor entero: x={x}")

# Módulo y asignación: /=
x %= 1.5
print(f"Dividimos el valor de x entre 3 y asignamos el valor del módulo: x={x}")

# Potencia y asignación: /=
x **= 3
print(f"Elevamos el valor de x a 3: x={x}")


# IDENTIDAD
# is
# is not
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(f"La lista a es la lista b? {list_a is list_b}")
print(f"La lista a no es la lista b? {list_a is not list_b}")

# PERTENENCIA
# in
# not in
list_a = [1, 2, 3]
print(f"El 4 está en la lista a? {4 in list_a}")
print(f"El 3 no está en la lista a? {3 not in list_a}")

# OPERADORES DE BIT - OPERADORES BINARIOS
a = 10  # 1010
b = 3  # 0011
# Sirven para trabajar con numeros enteros
print(f"AND: 10 & 3: {10 & 3}")  # 0010
print(f"OR: 10 | 3: {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3: {10 ^ 3}")  # 1001
print(f"NOT: ~10 : {~10}")  #
print(f"Desplazamiento a la derecha: 10 >> 2 = {10>>2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

# OPERADOR TERNARIO EN PYTHON
# Sintaxis: valor_si_true if condicion else valor_si_false

## -------------------------------------------
## TIPOS DE ESCTRUCTURAS DE CONTROL - EJEMPLOS
## -------------------------------------------

# CONDICIONALES
my_string = "Andrea"

if my_string == "Canmor115":
    print("my_string es 'Canmor115'")
elif my_string == "Camila":
    print("my_string es 'Camila'")
else:
    print("my_string no es 'Canmor115'")

# ITERATIVAS

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# EXCEPCIONES
try:
    print(10 / 1)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


## --------------------------------------------------------------------
## Función que imprime por consola todos los números comprendidos entre
#  10 y 55 (incluidos), pares y que no son ni el 16 ni múltiplos de 3
## --------------------------------------------------------------------
def my_function():
    for i in range(10, 56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)


my_function()
