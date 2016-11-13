#encoding: UTF-8
#Edgar Eduardo Alvarado Duran
#Problema 2

lista1 = []
lista2 = []

def main():
    n = int(input("Ingresa un valor"))
    while n != -1:
        lista1.append(n)
        lista2.append(n)
        n = int(input("Ingresa otro valor"))
    lista2.pop(len(lista1)-1)
    lista2.pop(0)
    print ("La lista original es", lista1, "y la nueva lista es", lista2)

main()