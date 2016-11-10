#encoding: UTF-8
#Adrian Tellez Lopez
#Tarea de Listas


#Primera funcion: Suma acumulada de una lista
def sumaLista(lista1):
    lista1A = []
    numero = 0
    for n in lista1:
        numero += n
        lista1A.append(numero)
    return lista1A

#Segunda funcion: Quitar el primer y ultimo dato de una lista
def quitarLista(lista2):
    lista2A=lista2[::]
    lista2A.pop()
    lista2A.reverse()
    lista2A.pop()
    lista2A.reverse()
    return lista2A

#Tercera funcion: Checar si los datos de una lista estan ordenados
def ordenarNumeros(lista3):
    lista3A = lista3 [:]
    lista3A.sort()
    if lista3A == lista3: 
        return True
    else:
        return False
    
#Cuarta funcion: Comparar si 2 palabras son anagramas            
def buscarAnagrama(lista4A, lista4B):
    palabra = list(lista4A)
    palabra1 = list(lista4B)
    palabraA = sorted(palabra)
    palabra1A = sorted(palabra1)
    if palabraA == palabra1A:
        return True
    else:
        return False

#Quinta funcion: Checar si una lista tiene un dato duplicado
def checarDuplicados(lista5):
    duplicado = 0
    for n in lista5:
        s = lista5.count(n)
        if s>1:
            duplicado += 1
    if duplicado >= 1:
        return True
    else:
        return False

#Sexta funcion: Quitar los numeros repetidos en una lista        
def eliminarRepetidos(lista6):
    for n in lista6:
        while lista6.count(n) > 1:
            lista6.remove(n)
    return lista6
    

def main():
    #Pruebas de la primera funcion
    lista1 = [1,2,3,4,5]
    print ("La lista", lista1, "regresa la lista acumulada:", sumaLista(lista1))
    lista1 = []
    print ("La lista", lista1, "regresa la lista acumulada:", sumaLista(lista1))
    lista1 = [5]
    print ("La lista", lista1, "regresa la lista acumulada:", sumaLista(lista1))
    
    #Pruebas de la segunda funcion
    lista2 = [1,4,7,2,0,9]
    print ("La lista", lista2, "sin el primer y ultimo dato es:", quitarLista(lista2))
    lista2 = ["A","E","I","O","U"]
    print ("La lista", lista2, "sin el primer y ultimo dato es:", quitarLista(lista2))
    lista2 = [1,1,1,6,7,9,1]
    print ("La lista", lista2, "sin el primer y ultimo dato es:", quitarLista(lista2))
    
    #Pruebas de la tercera funcion
    lista3 = [1,3,7,9,10]
    print("La lista", lista3, "esta ordenada:", ordenarNumeros(lista3))
    lista3 = [2,4,3,5,4,6,3]
    print("La lista", lista3, "esta ordenada:", ordenarNumeros(lista3))
    lista3 = [1,5,10,101,265]
    print("La lista", lista3, "esta ordenada:", ordenarNumeros(lista3))
    
    #Pruebas de la cuarta funcion
    lista4A = "Roma".lower()
    lista4B = "Amor".lower()
    print ("Las palabras", lista4A, "y", lista4B, "son anagramas:", buscarAnagrama(lista4A, lista4B))
    lista4A = "Hello".lower()
    lista4B = "Hola".lower()
    print ("Las palabras", lista4A, "y", lista4B, "son anagramas:", buscarAnagrama(lista4A, lista4B))
    lista4A = "Tarta".lower()
    lista4B = "Trata".lower()
    print ("Las palabras", lista4A, "y", lista4B, "son anagramas:", buscarAnagrama(lista4A, lista4B))
    
    #Pruebas de la quinta funcion
    lista5 = [1,3,6,4,8,0]
    print("La lista", lista5, "tiene duplicados:", checarDuplicados(lista5))
    lista5 = [1,1,2,2,3,3,4,4]
    print("La lista", lista5, "tiene duplicados:", checarDuplicados(lista5))
    lista5 = [1]
    print("La lista", lista5, "tiene duplicados:", checarDuplicados(lista5))
    
    #Pruebas de la sexta funcion
    lista6 = [1,2,6,4,3,2,9,10]
    print ("La lista sin duplicados es:", eliminarRepetidos(lista6))
    lista6 = [10,10,1,1,2,2,3]
    print ("La lista sin duplicados es:", eliminarRepetidos(lista6))
    lista6 = [5]
    print ("La lista sin duplicados es:", eliminarRepetidos(lista6))
    
main()        
        
        
        