#encoding: utf-8
#autor: Allan Sánchez 
#tarea 8 


#------------------------------------------------------------------
#esta función devuelve una lista con la suma acumulada de los datos

def nuevaListaSumaAcumulada (lista) : 
    nuevaLista = []
    if lista == nuevaLista :
        return nuevaLista        
    else :    
        nuevaLista.append(lista[0])
        for k in range (len(lista)-1) :
            suma = nuevaLista[k] + lista[k+1] 
            nuevaLista.append(suma)
        return nuevaLista

#------------------------------------------------        

#esta funcion quita el primer y el último dígito.                                                
def quitarValoresOrillas (lista) : 
    nuevaLista = lista[1:-1:]
    return nuevaLista

#-----------------------------------------------
 
#función que define si los valores entregados en una cadena estan ordenados.       
def estanOrdenados (cadena) :
    cadenaNormal = cadena
    cadenaOrdenada = cadena[::]
    
    cadenaOrdenada.sort()
    
    #print(cadenaNormal)
    #print(cadenaOrdenada)

    if cadenaNormal == cadenaOrdenada : 
        return True
    return False 
#------------------------------------------------- 

#función que identifica un anagrama; regresa True si lo es, False si no.      
def esAnagrama (palabra1,palabra2) : 
    palabraListada1 = []
    palabraListada2 = []
    
    if len(palabra1) == len(palabra2) : 
        for k in range (len(palabra1)) :
            palabraListada1.append(palabra1[k])
            palabraListada2.append(palabra2[k])
    
        palabraListada1.sort()
        palabraListada2.sort()
    
        if palabraListada1 == palabraListada2 : 
            return True
    return False 
    
#---------------------------------------------------    
#esta funcion recorre la lista y si encenra un dígito duplicado regresa true
def verificarDuplicados (lista) :
    for k in range (len(lista)): 
        repetido = lista.count(lista[k])
        if repetido > 1 :
            return True
        repetido = 0
    return False

#----------------------------------------------------
#función que elimina los datos repetidos y deja solo 1
def eliminarRepetidos (lista):
    a =""
    for k in sorted(lista):
        if k == a:
            lista.remove(k)
        a = k   
            
def main():
#----------listas---------
    lista1 = [2,1,3,4,5]
    lista2 = [1,2,3,4,5]
    lista3 = []
    lista4 = [5]
    lista5 = [1,2,3]
    lista6 = [1,2,1,4]
    lista7 = [1,2,3,5,6,3,8,8,1]
#----------listas----------

#---------palabras---------   
    palabra1 = "roma" #aqui cambia la palabra
    palabra2 = "Mora" #aqui cambia la palabra
    palabra3 = "holA"
    palabra4 = "hi"
    palabra5 = "perro"
    palabra6 = "repro"
    palabra_1 = palabra1.upper()
    palabra_2 = palabra2.upper()
    palabra_3 = palabra3.upper()
    palabra_4 = palabra4.upper()
    palabra_5 = palabra5.upper()
    palabra_6 = palabra6.upper()
#--------palabras------------

#--------lista con letras---------    
    cadena1 = ['A','B','C']
    cadena2 = ['A','X','B','F']
#--------lista con letras---------
    
    listaPrimerFuncion = nuevaListaSumaAcumulada (lista5)  
    print("La funcion 1 con la lista 5 da como resultado:",listaPrimerFuncion)
    listaPrimerFuncion = nuevaListaSumaAcumulada (lista4)  
    print("La funcion 1 con la lista 4 da como resultado:",listaPrimerFuncion)
    listaPrimerFuncion = nuevaListaSumaAcumulada (lista3)  
    print("La funcion 1 con la lista 3 da como resultado:",listaPrimerFuncion)
    
    print("------------------------------------------------------------")
    
    listaSegundaFuncion = quitarValoresOrillas (lista1)
    print ("La funcion 2 con la lista 1 da como resultado:",listaSegundaFuncion)
    listaSegundaFuncion = quitarValoresOrillas (lista5)
    print ("La funcion 2 con la lista 5 da como resultado:",listaSegundaFuncion)
    listaSegundaFuncion = quitarValoresOrillas (lista3)
    print ("La funcion 2 con la lista 3 da como resultado:",listaSegundaFuncion)
    
    print("------------------------------------------------------------")
    
    listasTercerFuncion = estanOrdenados (cadena1)
    print ("La funcion 3 con la cadena 1 da como resultado:",listasTercerFuncion)
    listasTercerFuncion = estanOrdenados (cadena2)
    print ("La funcion 3 con la cadena 2 da como resultado:",listasTercerFuncion)
    
    print("------------------------------------------------------------")
                          
    listasCuartaFuncion = esAnagrama(palabra_1,palabra_2)
    print("La funcion 4 con las palabras 1 y 2 da como resulado:",listasCuartaFuncion)
    listasCuartaFuncion = esAnagrama(palabra_3,palabra_4)
    print("La funcion 4 con las palabras 3 y 4 da como resulado:",listasCuartaFuncion)
    listasCuartaFuncion = esAnagrama(palabra_5,palabra_6)
    print("La funcion 4 con las palabras 5 y 6  da como resulado:",listasCuartaFuncion)
    
    print("------------------------------------------------------------")
    
    listasQuintaFuncion = verificarDuplicados (lista6)
    print("La funcion 5 con la lista 6 da como resultado:",listasQuintaFuncion) 
    listasQuintaFuncion = verificarDuplicados (lista7)
    print("La funcion 5 con la lista 7 da como resultado:",listasQuintaFuncion)
    listasQuintaFuncion = verificarDuplicados (lista2)
    print("La funcion 5 con la lista 2 da como resultado:",listasQuintaFuncion)
    
    print("------------------------------------------------------------")
    
    eliminarRepetidos(lista7)
    print("La funcion 6 cpn la lista 7 da como resultado:",lista7)
    eliminarRepetidos(lista6)
    print("La funcion 6 con la lista 6 da como resultado:",lista6)
    eliminarRepetidos(lista3)
    print("La funcion 6 con la lista 3 da como resultado:",lista3)
    

main()
