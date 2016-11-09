#encoding: UTF-8
#Autor; José Javier Rodríguez Mota
#Descripción: Tarea 8

#Sumas parciales
def sumarLista(nums):
    #Creamos una nueva lista
    listanueva=[]
    #Para cada dato en la lista inicial lo agregamos a la nueva
    #No ponemos listanueva=nums porque entonces modificamos la lista original
    for dato in nums:
        listanueva.append(dato)
    #Inicializamos el sumador    
    sumador=0
    #Ahora revisamos cada índice en la lista nueva
    for i in range(len(listanueva)):
        #A cada dato le sumamos el valor del sumador
        listanueva[i]+=sumador
        #El sumador se vuelve el valor del dato que acabamos de agregar
        sumador=listanueva[i]
    #Regresamos la lista    
    return listanueva
    
#Regresar la lista sin el primero ni el último dato    
def regresarMedio(nums):
    #Creamos una nueva lista
    listanueva=[]
    #Establecemos un loop que va del index 1(segundo dato) al penúltimo dato
    for i in range(1,len(nums)-1):
        #Agregamos a la lista estos datos
        listanueva.append(nums[i])
    #Regresamos la lista    
    return listanueva
    
#Revisamos el orden    
def revisarOrden(nums):
    #Vamos a comparar cada dato con el siguiente
    for i in range (len(nums)-1):
        #Vemos que el dato no sea mayor que el siguiente dato
        if (nums[i]>nums[i+1]):
            #En caso de serlo se detiene y regresa false
            return False
    #Si termina, regresa True        
    return True        

#Revisamos si son anagramas
def esAnagrama(string1,string2):
    #Primero eliminamos los espacios, en caso de que haya 
    prueba1=string1.replace(" ","")
    prueba2=string2.replace(" ","")
    #Revisamos en prueba 1 que todas las letras estén en el 2
    for letra in prueba1:
        #Si la letra no está en el otro o se repite más veces en uno que en otro regresa falso
        if letra.lower() not in prueba2.lower() or prueba1.lower().count(letra)!=prueba2.lower().count(letra):
            return False
    #Se debe revisar de igual forma el segundo con el primero        
    for letra in prueba2:
        if letra.lower() not in prueba1.lower() or prueba1.lower().count(letra)!=prueba2.lower().count(letra):
            return False
    #En caso de pasar ambos filtros regresa True
    return True    
    
#Eliminar repetidos        
def eliminarRepetidos(nums):
    #Vamos a revisar cada dato
    for dato in nums:
        #Vemos cuántos de cada dato hay
        if nums.count(dato)>1:
            #Eliminamos el dato en caso de estar repetido
            nums.remove(dato)
    #Regresamos la lista        
    return nums
    
#Función es repetido                       
def esRepetido(nums):
    #Sólo buscamos un repetido en la lista
    for dato in nums:
        #Vemos cuántos de cada dato hay
        if nums.count(dato)>1:
            #Detenemos el loop en cuanto haya un repetido
            return True
    #En caso de no haber, regresa false al terminar el loop        
    return False        

#Definimos main
def main():

    #Definimos nuestras múltiples listas
    lista1=[1,2,3,4,4,4,5]
    lista2=['A','B','X']
    lista3=[11,12,13,18,53,42,11]
    lista4=['A','B','C','D','D','E']
    lista5=[]
    lista6=[1,2]
    lista7=[1,2,3]
    
    #Probamos revisar orden
    if revisarOrden(lista1):
        print("Está ordenada la lista")
    else:
        print("No está ordenada la lista")    
    if revisarOrden(lista2):
        print("Está ordenada la lista")
    else:
        print("No está ordenada la lista")
    if revisarOrden(lista3):
        print("Está ordenada la lista")
    else:
        print("No está ordenada la lista")
    if revisarOrden(lista4):
        print("Está ordenada la lista")
    else:
        print("No está ordenada la lista")
    
    #Probamos la función de quitar el primero y el último
    print(regresarMedio(lista1))
    print(regresarMedio(lista2))
    print(regresarMedio(lista3))
    print(regresarMedio(lista4))
    print(regresarMedio(lista5))
    print(regresarMedio(lista6))
    print(regresarMedio(lista7))

    #Probamos la función de repetidos
    print(esRepetido(lista1))
    print(esRepetido(lista2))
    print(esRepetido(lista3))
    print(esRepetido(lista4))
    
    #Eliminamos repetidos
    eliminarRepetidos(lista1)
    eliminarRepetidos(lista2)
    eliminarRepetidos(lista3)
    eliminarRepetidos(lista4)
    
    #Imprimimos para ver que no hay repetidos
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    
    #Probamos la función de repetido nuevamente (teoricamente nos debe dar todo False)
    print(esRepetido(lista1))
    print(esRepetido(lista2))
    print(esRepetido(lista3))
    print(esRepetido(lista4))
    
    #Probamos la función sumar Lista
    print(sumarLista(lista1))
    print(sumarLista(lista3))
    print(sumarLista(lista5))
    
    #Imprimimos las listas para asegurarnos cómo quedaron
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    
    #Definimos nuestras strings
    string1="Hola"
    string2="Holloa"
    string3="Roma"
    string4="Mora"
    string5="armoniosamente"
    string6="enamoramientos"
    string7="frase"
    string8="Fresa"
    #Probamos el es anagrama
    if esAnagrama(string1,string2):
        print("%s y %s son anagrama"%(string1,string2))
    else:
        print("%s y %s no son anagrama"%(string1,string2))
    if esAnagrama(string3,string4):
        print("%s y %s son anagrama"%(string3,string4))
    else:
        print("%s y %s no son anagrama"%(string3,string4)) 
    if esAnagrama(string5,string6):
        print("%s y %s son anagrama"%(string5,string6))
    else:
        print("%s y %s no son anagrama"%(string5,string6))            
    if esAnagrama(string7,string8):
        print("%s y %s son anagrama"%(string7,string8))
    else:
        print("%s y %s no son anagrama"%(string7,string8))
#Corremos el programa
main()