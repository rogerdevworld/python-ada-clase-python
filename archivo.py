"""
Codelab: variables python
Codelab Variables Python

1 - Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso
2 - Crea un nuevo archivo .py
3 - Define una variable de cada tipo de primitivo

    3.1 - Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
    3.2 - Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
    3.3 - Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
    3.4 - Imprimir los resultados de las tareas anteriores
    3.5 - Envía el link del archivo en el repositorio con las respuesta
"""


texto = "Hola este es mi practica"
numero = 123

#respuesta 2 
max_int = ""

#boolean
boolean = True

#condicionales
if boolean:
    res = "verdad"
else:
    res = "mentira"
    
res_2 = "El valor max que acepta un int en python es "
res_3 = " esa informacion es  "

#respuesta 1 
res_con_1 = res_2 + max_int + res_3 + res
print(res_con_1)

#casting
text = "123" 
print(type(text))

numero = int(text)
print(type(numero))

text = str(numero)
print(type(text))


#respuesta 3.3

lista = []

add_numero = int(input("cantidad de numeros a sumar?"))

numero = 1

while numero <= add_numero:
    valor = int(input("Valores: "))
    lista.append(valor)
    numero+=1
suma = 0
par = 0
var = 0
while var < len(lista):
    if lista[var] % 2 == 1:
        suma += lista[var]
    else:
        par += lista[var]
    var += 1
print(f"Valor de la suma de los pares : {par}")
print(f"Valor de la suma de los impares : {suma}")