# stack sigue LIFO (last in first out) lo que significa que el último en entrar en el stack (pila) es el primero en salir
# ddddd
#
# pila:
#       5  (último elemento en ser añadido(push) pero tb será el primero en salir(pop))
#       4
#       3
#       2
#       1

# las operaciones más importantes que podemos realizar sobre los stacks son:
#
# pop()                 -> saca el elemento arriba de la pila (sería el primer elemento)
# append()              -> añade un elemento en el stack
# peek === stack[-1]    -> mira que elemento hay arriba de la pila ()

# EN PYTHON NO EXISTE UN BUILT-IN FUNCTION PARA IMPLEMENTAR STACKS


# Problem 1.
# Given a Path. The canonical path should have the following format:
# 1. starts with : /
# any two directories are separated by a single slash '/'
# Does not end with trailing '/'
# only contains the directories on the path from root directory to the target file or directory
#
# Given a path, return the canonical path
#
# Constraints
# * 1<= path.length<=3000
# path is a valid UNIX path
# path contains letters digits dots slashes and underscores


my_str = "dddd"

my_str[0] = 'D'
print(my_str)
