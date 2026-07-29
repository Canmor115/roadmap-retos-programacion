## FUNCIONES Y ALCANCE


# Funciones definidas por el usuario
# Simple
def greet():
    print("Hola python")


greet()


# Función con retorno
def return_greet():
    return "Hola python!"


print(return_greet())


# Funciones con argumentos
def arg_greet(greet, name):
    print(f"{greet} {name}!")


arg_greet("Hello", "Camila")

# Funciones con argumento predeterminado


def default_arg_greet(name="Python"):
    print(f"Hola {name}!")


default_arg_greet()

# Funciones con argumento y retorno


def default_args_greet(name="Python"):
    return f"Hola {name}!"


print(default_args_greet("Bea"))


# Con retorno de tupla de valores
def multiple_return():
    return "Hola", "Python"


greet, name = multiple_return()
print(greet)
print(name)


# Con número variable de argumentos
## El asterisco indica q podemos darle más de un parámetro
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!!!")


variable_arg_greet("Python", "Cami", "Bea")


# Con un número variable de argumentos con palabra clave
## Los dos asteriscos indica q podemos darle más de un parámetro ligada a una clave
def variable_key_arg_greet(**names):
    for (
        key,
        value,
    ) in names.items():
        print(f"{value} ({key})")


variable_key_arg_greet(language="Python", name="Cami", alias="Bea", age=36)

## -----------------------------
## FUNCIONES DENTRO DE FUNCIONES
## -----------------------------


## TOP INTERESTING
def outer_function():
    def inner_function():
        print("Función interna: Hola q ase")

    inner_function()


outer_function()


## ---------------------------------
## FUNCIONES DEL LENGUAJE (built-in)
## ---------------------------------
print(len("Camila"))
print(type(55.6))
print("Camila".upper())

## ---------------------------------
## Variables locales y globales
## ---------------------------------

global_variable = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var} {global_variable}")


hello_python()
print(global_variable)

## ---------
## EL EXTRA
## ---------


def print_numbers(text1, text2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count


print(print_numbers("Fizz", "Buzz"))
