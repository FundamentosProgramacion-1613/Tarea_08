#encoding: UTF-8
#Aldo Fuentes A01373294
#Tarea 08

def sumaAcumulada(lista):
    lstSuma = []
    acumulador = 0
    for n in range(1,len(lista)+1):
        for index in range (0,n):
            acumulador += lista[index]
        lstSuma.append(acumulador)
        acumulador = 0
    return lstSuma

def primeroUltimo(lista):
    listaN = []
    for n in range(1,len(lista)-1):
        listaN.append(lista[n])
    return listaN

def estaOrdenada(lista):
    ordenado = False
    if lista == sorted(lista):
        ordenado = True
    return ordenado

def esAnagrama(w1,w2):
    anagrama = False
    w1 = w1.replace(" ","")
    w2 = w2.replace(" ","")
    if sorted(list(w1.upper())) == sorted(list(w2.upper())):
        anagrama = True
    return anagrama

def valorDuplicado(lista):
    duplicado = False
    temp = ""
    for n in sorted(lista):
        if n == temp:
            duplicado = True
        temp = n 
    return duplicado

def quitarDuplicados(lista):
    temp = ""
    for n in sorted(lista):
        if n == temp:
            lista.remove(n)
        temp = n 
    return lista
    
def main():
    w1 = "Army"
    w2 = "Mary"
    w3 = "Roma"
    w4 = "Amor"
    w5 = "Roma y Army"
    w6 = "Amor y Mary"

    lista = [1,2,3,4,5]
    lista2 = [4,3,2,1,2,2]
    lista3 = [3,2,3]
    lista4 = [7,8]
    lista5 = [0,5,0,7]

    
    print("Problema 1")
    print("La lista:",lista,"regresa la lista acumulada:",sumaAcumulada(lista))
    print("La lista:",lista2,"regresa la lista acumulada:",sumaAcumulada(lista2))
    print("La lista:",lista3,"regresa la lista acumulada:",sumaAcumulada(lista3))
    print("La lista:",lista4,"regresa la lista acumulada:",sumaAcumulada(lista4))
    print("La lista:",lista5,"regresa la lista acumulada:",sumaAcumulada(lista5))
    print("\n")
    print("Problema 2")
    print("La lista:",lista,"regresa la lista sin el primer y ultimo valor:",primeroUltimo(lista))
    print("La lista:",lista2,"regresa la lista sin el primer y ultimo valor:",primeroUltimo(lista2))
    print("La lista:",lista3,"regresa la lista sin el primer y ultimo valor:",primeroUltimo(lista3))
    print("La lista:",lista4,"regresa la lista sin el primer y ultimo valor:",primeroUltimo(lista4))
    print("La lista:",lista5,"regresa la lista sin el primer y ultimo valor:",primeroUltimo(lista5))
    print("\n")
    print("Problema 3")
    print("La lista",lista,"esta ordenada:",estaOrdenada(lista))
    print("La lista",lista2,"esta ordenada:",estaOrdenada(lista2))
    print("La lista",lista3,"esta ordenada:",estaOrdenada(lista3))
    print("La lista",lista4,"esta ordenada:",estaOrdenada(lista4))
    print("La lista",lista5,"esta ordenada:",estaOrdenada(lista5))
    print("\n")
    print("Problema 4")
    print("Las cadenas:",w1,"/",w2,". Son un anagrama:",esAnagrama(w1,w2))
    print("Las cadenas:",w3,"/",w4,". Son un anagrama:",esAnagrama(w3,w4))
    print("Las cadenas:",w5,"/",w6,". Son un anagrama:",esAnagrama(w5,w6))
    print("Las cadenas:",w1,"/",w3,". Son un anagrama:",esAnagrama(w1,w3))
    print("Las cadenas:",w2,"/",w4,". Son un anagrama:",esAnagrama(w2,w4))
    print("\n")
    print("Problema 5")
    print("La lista:",lista,"tiene algun valor duplicado",valorDuplicado(lista))
    print("La lista:",lista2,"tiene algun valor duplicado",valorDuplicado(lista2))
    print("La lista:",lista3,"tiene algun valor duplicado",valorDuplicado(lista3))
    print("La lista:",lista4,"tiene algun valor duplicado",valorDuplicado(lista4))
    print("La lista:",lista5,"tiene algun valor duplicado",valorDuplicado(lista5))
    print("\n")
    print("Problema 6")
    print("La lista:",lista,"sin los valores duplicados es:")
    quitarDuplicados(lista)
    print(lista)
    print("La lista:",lista2,"sin los valores duplicados es:")
    quitarDuplicados(lista2)
    print(lista2)
    print("La lista:",lista3,"sin los valores duplicados es:")
    quitarDuplicados(lista3)
    print(lista3)
    print("La lista:",lista4,"sin los valores duplicados es:")
    quitarDuplicados(lista4)
    print(lista4)
    print("La lista:",lista5,"sin los valores duplicados es:")
    quitarDuplicados(lista5)
    print(lista5)
    print("\n")
    
main()
