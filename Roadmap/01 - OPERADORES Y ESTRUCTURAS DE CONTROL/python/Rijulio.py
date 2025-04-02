'''* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.'''

#En python los operadores , de asignación, bit a bit, de identidad, de pertenencia y booleanos

# Operadores aritmeticos:
suma = "+"
resta = "-"
multiplicacion = "*"
division = "/"
modulo = "%"
potenciacion = "**"
division_por_suelo = "//"

#Ejemplos:

e_suma = 12 + 12
e_resta = 24 - 12
e_multiplicacion = 6 * 2
e_division = 12 / 3
e_modulo = 12 % 5
e_potenciacion = 4**3
e_division_por_suelo = 12 // 7

resultados = (e_suma,e_resta,e_multiplicacion,
              e_division,e_modulo,e_potenciacion,
              e_division_por_suelo)

print (resultados)

#Operadores de comparacion:

mayor_que = ">" # Devuelve True si el operador de la izquierda es mayor que el operador de la derecha
menor_que = "<" # Devuelve True si el operador de la derecha es mayor que el operador de la izquierda
igual = "==" # Devuelve True si ambos operandos son iguales
mayor_igual = ">=" # Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
menor_igual = "<=" # Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha
diferente = "!=" # Devuelve True si ambos operandos no son iguales

# Ejemplos:

e_mayor_que1 = 12 > 6
e_mayor_que2 = 6 > 12

e_menor_que1 = 6 < 12
e_menor_que2 = 12 < 6

e_igual1 = 12 == 12
e_igual2 = 12 == 11

e_mayor_igual1 = 12 >= 6
e_mayor_igual2 = 12 >= 12
e_mayor_igual3 = 6 >= 12

e_menor_igual1 = 12 <= 6
e_menor_igual2 = 12 <= 12
e_menor_igual3 = 6 <= 12

e_diferente1 = 12 != 11
e_diferente2 = 12 != 12

ejemplos = (
    e_mayor_que1,e_mayor_que2,e_menor_que1,
    e_menor_que2,e_igual1,e_igual2,
    e_mayor_igual1,e_mayor_igual2,e_mayor_igual3,
    e_menor_igual1,e_menor_igual2,e_menor_igual3,
    e_diferente1,e_diferente2
)

print(ejemplos)

# Operadores logicos:

y = "and" # Devuelve True si ambos operandos son True
o = "or" # Devuelve True si uno de los dos operandos es True
no = "not" # Devuelve True si uno de los operandos es False

# Ejemplos:

e1 = True and True
e2 = True and False

e3 = True or True
e4 = False or True 
e5 = False or False 

e6 = not True 
e7 = not False

ejemplos2 = (e1,e2,e3,e4,e5,e6,e7)

print(ejemplos2)

# Operadores de asignacion ("=","+=","-=","*=","/=","**=","//=","%=","&=","|=","^=",">>=","<<=")

# Ejemplos

x = 50
x += 25
x -= 25
x *= 2
x /= 2
x **= 2
x //= 2
x %= 2
x = 50
x &= 10
x |= 25
x ^= 50
x >>= 5
x <<= 5

# Operdadores de membresia:

# Los operadores de membresia son tres: "in" y "not in"

# Ejemplos:

print(3 in (1,2,3))

print (3 not in (1,2,4,5))

# Operadores bitwise: "|","&","~","^",">>","<<"

# Ejemplos:

a = 0b1101
b = 0b1011
c = 40
d = 0b1000
e = 0b0001
print(bin(a & b))
print(bin(a | b))
print(bin(c))
print(bin(~c))
print(bin(a^b))
print(bin(d>>2))
print(bin(e<<3))

#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...

# Estructuras de control condicionales:
# Condicional "if":

aa = 8
bb = 2
if bb != 0 and type(bb) != type(str()):
    print(aa/bb)
elif bb == 0:
    print("No se puede dividir por cero.")
else:
    print("No se puede dividir un texto")

# El if tambien nos permite hacer estruturas condicionales de una sola linea

ab = 10
ab -= 1 if ab > 0 else ab
print(ab)

# Condicional "Match"

mes = 4
match mes:
    case 12 | 1 | 2: print("Invierno")
    case 3 | 4 | 5: print("Primavera")
    case 6 | 7 | 8: print("Verano")
    case 9 | 10 | 11: print("Otoño")
    case _: print("Error")
    
 
# Estructuras de control iterativas

# Ejemplo de bucle for simple
for i in "Python":
    if i == "h":
        continue
    print(i)

# Ejemplo de bucle for anidado

lista = [[1,2,3],
         [4,5,6],
         [7,8,9]]

for i in lista:
    print(f"Primer bucle")
    print(i)
    for j in i:
        print(f"Segundo bucle")
        print(j)
        
# Ejemplo de bucle for con el operador "range"

for i in range(10,55,2): # Donde 10 es el inicio de la secuencia 55 el final y 2 el salto entre iteraciones
    print(i)      
    
# Bucle while:

x = 5
while x > 0:
    x -= 1
    print(x)
else:
    print("El while ha terminado")

# Bucle while anidado
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0
    
z = 8
x = 1

# Arbol de navidad con el bucle while
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x +=2
    z-=1

# Estructuras de control excepcionales:

# Uso de raise:
# f = 4
# g = 4

# h = f/g

# print(h)
# raise ZeroDivisionError("No se puede dividir entre cero.")

# Uso de try y except

f = 4
g = 0

try:
    h = f / g
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("No ha ocurrido ninguna excepcion.")
finally:
    print("Bloque finally se ejecuta siempre que se coloque en un try.")
    
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

for num in range (10,56,2):
    if num == 16:
        continue
    elif num % 3 == 0:
        continue
    print(num) 
print(55) # En vista de que no se puede agregar el 55 al programa lo deje aca xD
