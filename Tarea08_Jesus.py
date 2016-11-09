#encoding: UTF-8
#Autor: Jesus Perea
#Tare8_Jesus

def sumaDeNumeros(lista):
    nueva = []
    numero = 0
    for i in lista:
        numero += i
        nueva.append(numero)
    return nueva
    
def borrarNumeros(lista):
    nueva = lista[:]
    suma = sum(nueva)
    if nueva:
        posicion = nueva[0]
        if suma == posicion:
            return nueva
        else:
            nueva.pop()
            nueva.pop(0)
            return nueva
    else:
        return nueva

def definirAnagrama(cadena1,cadena2):
    cadena1N = cadena1.lower()
    cadena2N = cadena2.lower()
    lista1 = list(cadena1N)
    lista2 = list(cadena2N)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else: 
        return False

def preguntarOrdenados(lista):
    nueva = lista[:]
    nueva.sort()
    if lista == nueva:
        return True
    else:
        return False
    
def preguntarDuplicados(lista):
    nueva = lista[:]
    nueva.sort()
    veces = 0
    for i in lista:
        cuenta = nueva.count(i)
        if cuenta > 1:
            veces += 1   
    if veces > 1:
        return True
    else:
        return False   

def eliminarRepetidos(lista):
    if lista:
        for i in lista:
            cuenta = lista.count(i)
            if cuenta > 1:
                lugar = lista.index(i,i)
                lista.pop(lugar)
                return lista
            else:
                respuesta = "No hay repetidos"
                return respuesta
    else:
        respuesta = "No hay repetidos"
        return respuesta
                                                         
def main():
    lista = [1,2,3,4,5]
    print("La lista es:",lista) 
    print("La suma de i+1 de la lista",sumaDeNumeros(lista))
    print("Lista si el primero y último",borrarNumeros(lista))
    cadena1 = "RoMa" #input("Teclea el supuesto anagrma")
    cadena2 = "mora" #input("Teclea el reves")
    print("La cadena 1 y 2 respectivamente son:",cadena1,"y",cadena2)
    print("¿Es Anagrama?",definirAnagrama(cadena1,cadena2))
    print("¿Están ordenados los números de la lista?",preguntarOrdenados(lista))
    print("¿Hay duplicados en la lista?",preguntarDuplicados(lista))
    print("Se han eliminado los repetidos:",eliminarRepetidos(lista))
    
main()