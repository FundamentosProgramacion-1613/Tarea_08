# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Tarea 8

# Función que devuelve una lista de las sumas acumuladas de un conjunto de datos que pertenecen a otra lista
def calcularSuma(lista):
    listaAcumulada = []
    sumatoria = 0
    for entero in lista:
        sumatoria += entero
        listaAcumulada.append(sumatoria)
    return listaAcumulada

# Función que a partir de una lista crea otra pero sin el primer ni último dato de aquélla recibida
def eliminarPU(lista):
    listaNueva = lista[::]
    if len(listaNueva) >= 2:
        listaNueva.remove(listaNueva[0])
        listaNueva.remove(listaNueva[len(listaNueva) - 1])
    elif len(listaNueva) == 1:
        listaNueva.remove(listaNueva[0])
    return listaNueva

# Función que determina si una lista está ordenada o no
def esOrdenada(lista):
    for i in range(0, len(lista)-1):
        if lista[i+1] < lista[i]:
            return False
    return True

# Función que determina si dos cadenas son anagramas
def sonAnagramas(cadena1, cadena2):
    caracteres1 = list(cadena1.lower())
    caracteres2 = list(cadena2.lower())
    for i in caracteres1:
        if i in caracteres2:
            caracteres2.remove(i)
        else:
            return False
    return(len(caracteres2) == 0)

# Función que determina si hay un dato duplicado en la lista
def hayDuplicados(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
    return False

# Función que elimina datos repetidos en una lista
def eliminarRepetidos(lista):
    lista.reverse()
    for i in lista:
        if lista.count(i) > 1:
            for k in range (0, lista.count(i)-1):
                lista.remove(i)
    lista.reverse()
    return lista

def main():
    #Listas y cadenas de pruebas
    lista1 = []
    lista2 = [7]
    lista3 = [1,2,3,4,5]
    lista4 = [11,11]
    lista5 = ["A", "R", "C"]
    lista6 = ["f", "g", "i", "k", "r"]
    lista7 = [0, 4, 6, 8, 4, 2]
    cadena1 = "Aretes"
    cadena2 = "Teresa"
    cadena3 = "Tere"
    cadena4 = "Tres"
    #Pruebas función calcularSuma
    print()
    print("La lista", lista1, "regresa la lista acumulada", calcularSuma(lista1))
    print("La lista", lista2, "regresa la lista acumulada", calcularSuma(lista2))
    print("La lista", lista3, "regresa la lista acumulada", calcularSuma(lista3))

    #Pruebas función eliminarPU
    print()
    print("Al eliminar el primer y último valor de la lista", lista1, "se obtiene la lista", eliminarPU(lista1))
    print("Al eliminar el primer y último valor de la lista", lista3, "se obtiene la lista", eliminarPU(lista3))
    print("Al eliminar el primer y último valor de la lista", lista4, "se obtiene la lista", eliminarPU(lista4))

    #Pruebas función esOrdenada
    print()
    print("Es", esOrdenada(lista3), "que la lista", lista3, "está ordenada")
    print("Es", esOrdenada(lista6), "que la lista", lista6, "está ordenada")
    print("Es", esOrdenada(lista5), "que la lista", lista5, "está ordenada")

    #Pruebas función sonAnagramas
    print()
    print("Es", sonAnagramas(cadena1, cadena2), "que la cadena", cadena1, "y la cadena", cadena2, "son anagramas")
    print("Es", sonAnagramas(cadena2, cadena3), "que la cadena", cadena2, "y la cadena", cadena3, "son anagramas")
    print("Es", sonAnagramas(cadena4, cadena3), "que la cadena", cadena4, "y la cadena", cadena3, "son anagramas")

    #Pruebas función hayDuplicados
    print()
    print("En la lista", lista4, "es", hayDuplicados(lista4), "que hay datos duplicados")
    print("En la lista", lista1, "es", hayDuplicados(lista1), "que hay datos duplicados")
    print("En la lista", lista7, "es", hayDuplicados(lista7), "que hay datos duplicados")

    #Pruebas función eliminarRepetidos
    print()
    print("Al eliminar los valores de repetidos de la lista", lista3)
    print("se obtiene la lista", eliminarRepetidos(lista3))
    print("Al eliminar los valores de repetidos de la lista", lista4)
    print("se obtiene la lista", eliminarRepetidos(lista4))
    print("Al eliminar los valores de repetidos de la lista", lista7)
    print("se obtiene la lista", eliminarRepetidos(lista7))

main()