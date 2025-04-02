#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */

#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

# Funciones basicas en python:

# Funciones sin parametros ni retorno
def saludar ():
    print ('Hola!')
    
def despedir ():
    print ('Adios!')

saludar()
despedir()

# Funciones con parametros sin retorno

def conocer (nombre):
    print (f'Hola {nombre}')
    
def conocer2 (nombre, apellido):
    print(f'Hola {nombre} {apellido} un gusto conocerte.') 
    
conocer('Juan')
conocer2('Juan','Sanchez')

# Funciones con retorno

def sumar (a,b,c=0): 
    suma = a+b+c
    return suma

def restar (a,b,c=0):
    resta = a-b-c
    return resta

print(sumar(20,50)) # En este caso en una misma funcion puedo llamar a dos o tres parametros
print(sumar(20,50,18)) # definiendo en la funcion que el ultimo valor es igual a 0


print(restar(100,50))
print(restar(100,50,18))

# - Comprueba si puedes crear funciones dentro de funciones.

def sumar_resultados(a,b): # En el caso de python se pueden crear funciones dentro de funciones  
    def suma(a1,a2):       # Y retornar los resultados de las mismas.
        suma = a1 + a2
        return suma
    
    def resta(b1,b2):
        resta = b1 - b2
        return resta
    
    a1,a2 = a/2,a/2
    b1,b2 = b/2,b/3
    
    return(suma(a1,a2)+resta(b1,b2))

print(sumar_resultados(100,50))

#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

# En python hay distintos tipos de funciones integradas, numericas, cadenas de texto, etc.

# Funciones numericas:

ent = 10
flot = 5.0

print (int(flot)) # La funcion int convierte un numero flotante o decimal a uno entero
print (float(ent)) # La funcion float convierte una numero entero a uno decimal asignando un '.0'

# Funciones de cadenas

texto = 'Hola mundo'

print(len(texto)) # Devuelve la cantidad de caracteres que tiene el texto
print(texto.upper()) # Devuelve el texto transformado todo a mayusculas
print(texto.lower()) # Devuelve el texto transformado todo a minusculas

#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

# Las variables globales son aquellas que se declaran fuera de una funcion y son accesibles
# desde cualquier parte de la estrucutra del codigo. En cambio las variables locales son aquellas
# que forman parte de una funcion y solo se puede acceder a ellas en la funcion.

x = 10 # Esta es una variable global

def mostrarx():
    print('El valor de x es:',x) # Por ejemplo desde una funcion
    
mostrarx()

def mostrary():
    y = 20 # Esta en cambio es una variable local
    print(f'el valor de y es:{y}') # a la cual solo se puede acceder a traves de la funcion

mostrary()

z = 20

# def mostrarz():
#     z = z + 2 ---> una particularidad es que no se puede modificar una variable global desde una funcion
#     print('El valro de z es', z) o por lo menos no de esta manera
    
# mostrarz()

def mostrarz():
    global z # Esta es la forma correcta de modificar una variable global desde una funcion
    z += 2
    print('Elvalor de z es:',z)
    
mostrarz()

# def a():
#     a = 10 

# def mostrara():
#     print('el valor de a es:', a) ---> y si quiero acceder a una variable local como una global
# se hace de la siguiente manera
    
# mostrara()

def a():
    global a
    a = 10 

a()
   
def mostrara():
    print('el valor de a es:', a)
    
mostrara()

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def texto_numeros(cadena1, cadena2):
    repeticiones = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{cadena1} {cadena2}') 
            repeticiones.append(cadena1)
            repeticiones.append(cadena2)
        elif i % 5 == 0:
            print(f'{cadena2}')
            repeticiones.append(cadena2)
        elif i % 3 == 0:
            print(f'{cadena1}')
            repeticiones.append(cadena1)
        else:
            print(i)    
    return len(repeticiones)

print(texto_numeros('Este numero es multiplo de 3','Este numero es multiplo de 5')) 
