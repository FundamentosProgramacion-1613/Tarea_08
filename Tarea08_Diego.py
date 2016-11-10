#encoding:UTF-8
#By Diego Perez
#Funciones de Listas

#1. ACUMULAR VALORES DE LA LISTA

def listaAcumulada(lista):
    listaNueva = []
    contador = 0

    if len(lista) > 1 or len(lista) == 0:
        for x in lista:
            contador +=lista[x-1]
            listaNueva.insert(x,contador)
    else:
        contador +=lista[0]
        listaNueva.insert(0,contador)
    return(listaNueva)

#2. ACUMULAR VALORES DE LA LISTA        
def sinPyUValor(lista):
    listaNueva = lista[:]
    listaNueva.pop(0)
    listaNueva.pop(len(listaNueva)-1)
    return listaNueva

#3. Comprobar si lista esta ordenada
def listaOrdenada(lista):
    listaNueva = lista[:]
    listaNueva.sort()
    if (listaNueva == lista):
        return True
    else:
        return False
    
#4. Comprobar Anagrama
def comprobarAnagrama(string1,string2):

    lista1 = list(string1.upper())
    lista2 = list(string2.upper())
    lista1.sort()
    lista2.sort()
    
    if (lista1 == lista2):
        return True
    else:
        return False
#5. Comprobar Valores Duplicados
    
def comprobarDuplicados(lista):
    duplicado = False
    lista.sort()
    
    lastValue = ""
    if len(lista) > 1:
        for element in lista:
            if element == lastValue:
                duplicado = True
            lastValue = element
    return duplicado
        
#6. Borrar Valores Duplicados
def borrarDuplicados(lista):
    lista.sort()
    lastValue = ""

    for element in lista:
        if element == lastValue:
            lista.remove(element)
        lastValue = element           

    return lista

def main():
    #Listas/cadenas demo
    lista1 = [1,2,3,4,5]
    lista2 = [5]
    lista3 = [1,2]
    lista4 = [1,2,5,4]
    lista5 = [1,1,1,2]
    lista6 = [1,2,3,2,4]
    lista7 = [1,2,5,5,7]
    #Probar Funcion 1 
    print("PRUEBAS FUNCION 1")
    print(listaAcumulada(lista1))
    print(listaAcumulada(lista2))
    #Probar Funcion 2 
    print("PRUEBAS FUNCION 2")    
    print(sinPyUValor(lista1))
    print(sinPyUValor(lista3))
    #Probar Funcion 3 
    print("PRUEBAS FUNCION 3")
    print(listaOrdenada(lista1))
    print(listaOrdenada(lista4))
    #Probar Funcion 4
    print("PRUEBAS FUNCION 4")
    print(comprobarAnagrama("ana","naa"))
    print(comprobarAnagrama("Mora","Roma"))
    print(comprobarAnagrama("Hello","Hola"))
    #probar Funcion 5
    print("PRUEBAS FUNCION 5")
    print(comprobarDuplicados(lista7))
    print(comprobarDuplicados(lista1))
    #probar Funcion 6
    print("PRUEBAS FUNCION 6")
    print(borrarDuplicados(lista7))
    print(borrarDuplicados(lista6))
    print(borrarDuplicados(lista2))
main()
