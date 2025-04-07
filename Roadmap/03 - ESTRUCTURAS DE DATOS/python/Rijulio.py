#   * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.

# En python existen varios tipos de estructuras de datos: listas, tuplas, diccionarios y conjuntos

#Listas y sus metodos:

frutas = ['manzana','pera','mango','manzana','mango','banana'] # Lista 
print(frutas.count('mango')) # La funcion count() cuenta el numero de veces que aparece el valor indicado
print(frutas.count('mandarina'))
print(frutas.index('manzana')) # La funcion index() retorna la posicion del valor indicado
print(frutas.index('manzana',1)) # En este caso nos permite retornar la posicion siguiente a una posicion especifica

frutas.reverse() # La funcion reverse() reordena la lista a la inversa
print(frutas)

frutas.append('piña') # La funcion append() nos permita agregar nuevos elementos al final de la lista 
print(frutas)

frutas.sort() # La funcion sort() reordena la lista en este caso en orden alfabetico
print(frutas)

frutas.pop() # La funcion pop() elimina el ultimo elemento de la lista en caso de no haber indicado un indice
print(frutas)

# Las listas ademas tienen distintas formas de usarse
# Usar listas como pilas (last-in, first-out)

pila =[1,2,3]
print(pila)
pila.append(4)
pila.append(5)
print(pila)

pila.pop()
pila.pop()
print(pila)

# Usar listas como colas (first-in, first-out)

from collections import deque

cola = deque(['eren','mikasa','armin'])
cola.append('annie')
cola.append('jean')
print(cola)

cola.popleft()
cola.popleft()
print(cola)

# Tuplas y sus metodos:
# Las tuplas aunque se parecen mucho a las listas son inmutables.
tupla = (123, 321, 'shinzou wo sasageyo') 
# tupla[2] = 456 ---> Por lo que este condigo nos da un error

print(tupla)

# Las tuplas ademas se pueden anidar

tu = (tupla, 'Paradis', 'Marley')
print(tu)

# Conjuntos:
# Una particularidad del los conjuntos es que no admiten datos repetidos, por lo que los hace utiles para 
# la verificacion de pertenencia y la eliminacion de entradas duplicadas
carrito = {'harina','pasta','arroz','manteca','harina','arroz'}
print(carrito)

print('arroz' in carrito) # Esta es una comprobacion rapida de membresia
print('jamon' in carrito)

a = set('abracadabra')
b = set('alacazam')
print(a,b)

# Una particularidad de los conjuntos es que se pueden hacer operacones con ellos por ejemplo:

print(a - b) # Letras en "a" que no estan en "b"
print(a | b) # Letras en "a" o en "b" o en ambos
print(a & b) # Letras que estan en "a" y en "b"
print(a ^ b) # Letras que estan en "a" o en "b" pero no en ambos

# Diccionarios:

# Los diccionarios se caracterizan por tener una estructura de "clave:valor"
dic = {'clave':'valor',
       'luis':18,
       'moises':13,
       'fabian':8,
       'nairim':3}

print(dic)
dic['marilyn'] = 45 # ---> Se añaden valores de esta manera
print(dic)
del dic['marilyn'] # ---> Y se eliminan de esta otra
print(dic)

print(list(dic)) # ---> Asi se imprime en pantalla las claves
print(sorted(dic)) # ---> Asi se imprimen en orden alfabetico
print('luis' in dic)
print('marilyn' in dic)

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.

agenda = {}
def contador(numero):
    cantidad = []
    for i in numero:
        cantidad.append(i)
        
    return len(cantidad)

print('Desea:\na) Añadir un nuevo contacto\nb) Eliminar un contacto\nc) Buscar un contacto\nd) Actualizar un contacto.\ne) Ver agenda completa\nf) Salir.')
opcion = input(str())
while  opcion == 'a' or 'b' or 'c' or 'd' or 'e':
    
    if opcion == 'a':
        nombre = input(str('Introduzca el nombre del contacto: \n'))
        telefono = input(str('Introduzca el numero de telefono: \n'))
        while (contador(telefono)) != 11:
            telefono = input(str('Introduzca un numero de 11 digitos: \n'))
        
        agenda [nombre] = telefono
        print(f'El contacto {nombre} ha sido añadido.')
        
    
    elif opcion == 'b':  
        nombre = input(str('Introduzca el nombre del contacto a eliminar: \n'))
        if (nombre in agenda) == True:
            
            for i in agenda:
                if i == nombre:
                    del agenda[nombre]
                    for i in agenda:
                        print(i,agenda[i])
                    break
                else:
                    continue
        else:
            print(f'No se ha encontrado a {nombre} en la agenda.')
                
    elif opcion == 'c':
        nombre = input(str('Introduzca el nombre del contacto: \n'))
        if (nombre in agenda) == True:
            
            for i in agenda:
                if i == nombre:
                    print(agenda[nombre])
                    break
                elif i != nombre:
                    continue
        else:
            print(f'No se ha encontrado a {nombre} en la agenda.')
                   
    elif opcion == 'd':
        nombre = input(str('Introduzca el nombre del contacto: \n'))
        if (nombre in agenda) == True:
            
            for i in agenda:
                if i == nombre:
                    nuevo_num = input(str('Introduzca el nuevo numero: \n'))
                    agenda[i] = nuevo_num
                else:
                    continue
        else:
            print(f'No se ha encontrado a {nombre} en la agenda.')
    elif opcion == 'e':
        for i in agenda:
            print(i,agenda[i])                
    else: 
        print('Hasta luego.')
        break
    opcion = input(str('Desea:\na) Añadir un nuevo contacto\nb) Eliminar un contacto\nc) Buscar un contacto\nd) Actualizar un contacto.\ne) Ver agenda completa\nf) Salir.\n'))
