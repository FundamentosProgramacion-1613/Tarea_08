#encoding:UTF-8
#Lenin Silva Gutiérez A01373214
#Tarea 08: Listas

def sumarLista(lista):
    n_lista = lista[:1]
    for i in range(1, len(lista)):
        n_lista.append(lista[i]+n_lista[i-1])
        
    return n_lista
    
def quitarPrimeroUltimo(lista):
    n_lista = lista[1:len(lista)-1]
    return n_lista
    
def esOrdenada(lista):
    n = lista[:]
    n.sort()
    #print (n)
    if lista == n:
        return True
    else:
        return False
    """La siguiente opción funciona en tanto la lista no contenga datos de más
    de un caracter (ej. 'BAX','dct','CjZ')
    anterior = 0
    for i in lista:
        dato = ord(str(i))
        if anterior>dato:
            return False
        anterior = dato
    return True"""
    
def esAnagrama(cadena1,cadena2):
    cadena1=cadena1.lower()
    cadena2=cadena2.lower()
    
    c2 = list(cadena2)
    for i in cadena1:
        if i in c2:
            c2.remove(i)#Así revisa que haya la misma cantidad de una letra
        else:
            return False
    if len(c2)>0:
        return False
    return True

def estaDuplicado(lista):
    for i in lista:
        if lista.count(i)>=2:
            return True
    return False

def eliminarRepetidos(lista):
    for i in lista:
        while lista.count(i)>1:
            lista.remove(i)

def main():

    #Pruebas función 1
    prueba1_1 = [4,5,6,8,10]
    prueba1_2 = []
    prueba1_3 = [543]
    prueba1_4 = [5,4,3,2,1]
    
    print ("Función 1")
    print()
    
    print ("La lista ", prueba1_1," regresa la lista acumulada ", sumarLista(prueba1_1))
    print ("La lista ", prueba1_2, " regresa la lista acumulada ", sumarLista(prueba1_2))
    print ("La lista ", prueba1_3, " regresa la lista acumulada ", sumarLista(prueba1_3))
    print ("La lista ", prueba1_4, " regresa la lista acumulada ", sumarLista(prueba1_4))
    print()
    
    #Pruebas función 2
    p2_1 = [4,5,23,82,10]
    p2_2 = [254]
    p2_3 = [545,282]
    p2_4 = []
    
    print ("Función 2")
    print()
    
    print("La lista ", p2_1, " regresa la lista ", quitarPrimeroUltimo(p2_1))
    print("La lista ", p2_2, " regresa la lista ", quitarPrimeroUltimo(p2_2))
    print("La lista ", p2_3, " regresa la lista ", quitarPrimeroUltimo(p2_3))
    print("La lista ", p2_4, " regresa la lista ", quitarPrimeroUltimo(p2_4))
    print()
    
    #Pruebas función 3
    p3_1 = [4,5,23,82,10]
    p3_2 = [254,438,926]
    p3_3 = ["XJ", "BA", "jis"]
    p3_4 = ["A","J","K","Z"]
    
    print ("Función 3")
    print()
    
    if esOrdenada(p3_1):
        print ("La lista ",p3_1, " está ordenada")
    else:
        print ("La lista ", p3_1, " no está ordenada")
        
    if esOrdenada(p3_2):
        print ("La lista ", p3_2," está ordenada")
    else:
        print("La lista ", p3_2, " no está ordenada")
        
    if esOrdenada(p3_3):
        print ("La lista ", p3_3," está ordenada")
    else:
        print ("La lista ", p3_3, " no está ordenada")
        
    if esOrdenada(p3_4):
        print ("La lista ", p3_4, " está ordenada")
    else:
        print ("La lista ", p3_4, " no está ordenada")
        
    print()
        
    #Pruebas función 4
    s1_1 = "corazon"
    s1_2 = "zocaron"
    s2_1 = "campeon"
    s2_2 = "empaconon"
    s3_1 = "Cantar"
    s3_2 = "Tranca"
    s4_1 = "aguacate"
    s4_2 = "agresiva"
    
    if esAnagrama(s1_1,s1_2):
        print ("%s y %s son anagramas"%(s1_1,s1_2))
    else:
        print ("%s y %s no son anagramas"%(s1_1,s1_2))
        
    if esAnagrama(s2_1,s2_2):
        print("%s y %s son anagramas"%(s2_1,s2_2))
    else:
        print ("%s y %s no son anagramas"%(s2_1,s2_2))
        
    if esAnagrama(s3_1,s3_2):
        print ("%s y %s son anagramas"%(s3_1,s3_2))
    else:
        print("%s y %s no son anagramas"%(s3_1,s3_2))
        
    if esAnagrama(s4_1,s4_2):
        print("%s y %s son anagramas"%(s4_1,s4_2))
    else:
        print("%s y %s no son anagramas"%(s4_1,s4_2))
        
    print()
    
    #Pruebas función 5
    p5_1 = [4,5,23,82,4,82]
    p5_2 = [5,6,8,10,86]
    p5_3 = [83,98,83,83,10,84]
    p5_4 = []
    
    print("Función 5")
    print()
    
    if estaDuplicado(p5_1):
        print ("La lista ", p5_1, " tiene datos duplicados")
    else:
        print ("La lista ", p5_1, " no tiene datos duplicados")
        
    if estaDuplicado(p5_2):
        print("La lista ", p5_2," tiene datos duplicados")
    else:
        print ("La lista ", p5_2, " no tiene datos duplicados")
        
    if estaDuplicado(p5_3):
        print ("La lista ", p5_3, " tiene datos duplicados")
    else:
        print ("La lista ", p5_3, " no tiene datos duplicados")
        
    if estaDuplicado(p5_4):
        print("La lista ", p5_4, " tiene datos duplicados")
    else:
        print ("La lista ", p5_4, " no tiene datos duplicados")
        
    print()
    
    #Pruebas función 6
    p6_1 = [1,1,1,1,2,2,2,2,3,3,3,4,5,6]
    p6_2 = [83,23,15,54]
    p6_3 = [5,6,7,7,6,5]
    p6_4 = [8,9,10,8,8,9]
    
    print ("Función 6")
    print()
    
    print (p6_1,end ="-->")
    eliminarRepetidos(p6_1)
    print (p6_1)
    
    print (p6_2,end="-->")
    eliminarRepetidos(p6_2)
    print(p6_2)
    
    print(p6_3, end="-->")
    eliminarRepetidos(p6_3)
    print(p6_3)
    
    print(p6_4, end="-->")
    eliminarRepetidos(p6_4)
    print(p6_4)

main()        