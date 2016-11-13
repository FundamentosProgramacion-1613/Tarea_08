#encoding: UTF-8
#Edgar Eduardo Alvarado Duran
#Problema 1

def main():
    lista = []
    lista1 = []
    n = int(input("Ingresa un numero"))
    while n != -1:
        lista.append(n)
        lista1.append(sum(lista))
        n = int(input("Ingresa un numero"))
    print ("La lista es", lista, "y su suma es", lista1)
    
main()