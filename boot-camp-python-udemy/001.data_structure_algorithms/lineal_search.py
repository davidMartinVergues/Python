import random

def lienal_search(lista,goal):
    match = False

    for element in lista:
        if element == goal:
            match = True
            break
    return match


# está bien poner el break pero en realidad si nos ponemos en el peor de los
#  casos, que es cómo debemos proceder, q sería que el goal no se encuentra o está al final 
# de la lista, ese break no sirve.


if __name__ == "__main__":
    list_size   = int(input('indica el tamaño de la lista\n'))
    goal        = int(input('indica el número q quieres buscar\n'))

    myList= [random.randint(0,100) for i in range(list_size)]
    print(sorted(myList))

    find_out = lienal_search(myList,goal)

    print(f'el elemento objetivo {goal} {"lo hemos encontrado en la lista" if find_out else "no se encuentra en la lista"}')