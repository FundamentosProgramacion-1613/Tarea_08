#encoding: UTF-8
#Autor: Luis Martín Barbosa Galindo
#Tarea 8

#En esta funcion vamos a sumar los valores de la lista
"""def ejercicio1(lista1):
    lista1b = []
    if len(lista1) == len(lista1b):
        return lista1
    else:
        for i in range(len(lista1)):
            n = lista1[i+1] + lista1b[i]
            lista1b.append(n)
        return lista1b"""
    
#En esta funcion vamos a quitar el primer y el ultimo digito de la lista
def ejercicio2(lista2):
    lista2.pop()
    lista2.pop(0)
    return lista2
    
#En esta funcion buscamos que este en orden la lista
def ejercicio3(lista3):
    lista_o = lista3[::]
    lista_o.sort()
    if listae == lista3 :
        return True
    else:
        return False
    
#En esta funcion vemos si las palabras en la listas son anagramas
def ejercicio4(lista4a,lista4b):
    palabra1 = []
    palabra2 = []
    for p in range(len(lista4a)):
        palabra1.append(lista4a[p])
        palabra2.append(lista4b[p])
            
    palabra1.sort()
    palabra2.sort()
    if palabra1 == palabra2:
        return True
    else:
        return False

#En esta funcion la lista sera analizada y buscara si esta repetido un elemento                
def ejercicio5(lista5):
    for n in range(len(lista5)):
        u_r= lista5.count(lista5[n])
    if u_r == 1:
        return False
    else:
        return True
 
 #en esta funcion la lista se analiza y se quitan los elementos repetidos
 def ejercicio6(lista6):
    lista6.sort()
    for n in range(len(lista6)):
        u_r= lista6.count(lista6[n])
        if u_r > 1:
            lista.remove(u_r)
        else:
         print("¿Wut?")
             
def main():
    
    print("Ejercicio número 1")
    lista1 = [1,2,3]
    ejercicio1(lista1)
    print (lista1b)
    lista1 = []
    ejercicio1(lista1)
    print(lista1)
    lista1 = [5]
    ejercicio1(lista1)
    print(lista1)
    print("Ejercicio número 2")
    lista2 = [1,2,3,4,5]
    ejercicio2(lista2)
    print(lista2)
    lista2 = [1,2]
    ejercicio2(lista2)
    print(lista2)
    lista2 = [7,8,9,10]
    ejercicio2(lista2)
    print (lista2)
    print("Ejercicio número 3")
    lista3=[1,2,3]
    ejercicio3(lista3)
    lista3=[5,4,3]
    ejercicio3(lista3)
    lista3=["A","X","B"]
    ejercicio3(lista3)
    print("Ejercicio número 4")
    lista4a=["Roma"]
    lista4b=["Mora"]
    ejercicio4(lista4a,lista4b)
    lista4a=["Hola"]
    lista4b=["Hello"]
    ejercicio4(lista4a,lista4b)
    lista4a=["Hoy"]
    lista4b=["Yo"]
    ejercicio4(lista4a,lista4b)
    print("Ejercicio número 5")
    lista5 = [1,2,3,4,5]
    ejercicio5(lista5)
    lista5 = [11,1,2,3,11]
    ejercicio5(lista5)
    lista5 = []
    ejercicio5(lista5)
    print("Ejercicio número 6")
    lista6 = [1,2,3,4,6,3]
    ejercicio6(lista6)
    print(lista6)
    lista6 = [5,4,5,3,2,1]
    ejercicio6(lista6)
    print lista6
    lista6 = [3,4,5,6,7,8,6]
    ejercicio6(lista6)
    print(lista6)
    
main()
