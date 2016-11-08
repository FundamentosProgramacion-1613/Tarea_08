#encoding: UTF-8
#Autor; José Javier Rodríguez Mota
#Descripción: Tarea 8
def sumarLista(nums):
    listanueva=nums
    sumador=0
    for i in range(len(listanueva)):
        listanueva[i]+=sumador
        sumador=listanueva[i]
    return listanueva
def regresarMedio(nums):
    listanueva=nums
    listanueva.pop(0)
    listanueva.pop(-1)
    return listanueva
def revisarOrden(nums):
    for i in range (len(nums)-1):
        if (nums[i]>nums[i+1]):
            return False
    return True        
def esAnagrama(string1,string2):        
def main():
    print(revisarOrden(['A','B','X']))
main()