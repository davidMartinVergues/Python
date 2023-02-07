import random


def binary_search(lista,start,end,goal,counter):

    counter+=1

    print(f'buscando el {goal} entre {lista[start]} - {lista[end]}')
    
    if start>=end:
        return False,counter

    mean = (start+end)//2
    
    if lista[start] == goal:
        return True,counter
    if lista[end] == goal:
        return True,counter
    if lista[mean] == goal:
        return True,counter
    

    if lista[mean]< goal:
        start = mean+1
        end = end-1
        return binary_search(lista,start, end,goal,counter)
    else:
        start = start+1
        end = mean-1
        return binary_search(lista,start, end,goal,counter)
    
def binary_search2(lista,goal,start,end,counter):
    
    counter+=1

    if start is None:
        start = 0
    if end is None:
        end = len(lista)-1
    
    midpoint = (start + end)//2

    if end < start:
        return -1,counter
    elif lista[midpoint] == goal:
        print(f'binary_search_2 => buscando el {goal} entre {lista[start]} - {lista[end]}')
        return midpoint,counter
    elif lista[midpoint] > goal:
        print(f'binary_search_2 => buscando el {goal} entre {lista[start]} - {lista[end]}')
        return binary_search2(lista,goal,start,midpoint-1, counter)
    else:
        print(f'binary_search_2 => buscando el {goal} entre {lista[start]} - {lista[end]}')
        return binary_search2(lista,goal,midpoint+1,end,counter)


# está bien poner el break pero en realidad si nos ponemos en el peor de los
#  casos, que es cómo debemos proceder, q sería que el goal no se encuentra o está al final 
# de la lista, ese break no sirve.


if __name__ == "__main__":
    list_size   = int(input('indica el tamaño de la lista\n'))
    goal        = int(input('indica el número q quieres buscar\n'))

    myList= sorted([random.randint(0,100) for i in range(list_size)])
    print(sorted(myList))

    find_out    = binary_search(myList,0,len(myList)-1,goal,0)
    find_out_2  = binary_search2(myList,goal,0,len(myList)-1,0)

    print(f'el elemento objetivo {goal} {"lo hemos encontrado en la lista" if find_out[0] else "no se encuentra en la lista"} con un total de pasos de {find_out[1]}')
    print(f'el elemento objetivo {goal} {"lo hemos encontrado en la lista" if find_out_2[0]!=-1 else "no se encuentra en la lista"} con un total de pasos de {find_out_2[1]}')