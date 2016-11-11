#encoding: UTF-8
#Autor: Hector David Hernandez Rodriguez
#Tarea 8


#1
def nuevaListaAcumulable (lista) : 
    nuevaLista=[]
    if lista == nuevaLista:
        print (nuevaLista)       
    else :    
        nuevaLista.append(lista[0])
        for n in range (len(lista)-1) :
            sumatoria = lista[n+1] + nuevaLista[n] 
            nuevaLista.append(sumatoria)
        print (nuevaLista)

#2     
                        
def eliminarExtremos (lista) : 
    nuevaLista = lista[1:-1:]
    print(nuevaLista)

#3
    
def Ordenar (cadena) :
    nuevaCadena = cadena[::]
    
    nuevaCadena.sort()
    if cadena == nuevaCadena : 
        return True
    else:
        return False 
    
#4   


def definirAnagrama (P1,P2) : 
    pList = []
    pList2 = []
    P1.upper()
    P2.upper()
    for l in range (len(P1)) :
        pList.append(P1[l])
        pList2.append(P2[l])
    
    print(pList)
    pList.sort()
    pList2.sort()
    
    if pList == pList2 : 
        return True
    else:
        return False 
#7 
def main ():
    lista = [1,2,3,4,5]
    
    nuevaListaAcumulable (lista)  
    print(nuevaListaAcumulable)
    
    eliminarExtremos (lista) 
     
    cadena = ['A','B','C']
    Ordenar (cadena)
    print (Ordenar(cadena))
    
    P1 = "Hablar"
    P2 = "hallar"
    definirAnagrama(P1,P2)

main()