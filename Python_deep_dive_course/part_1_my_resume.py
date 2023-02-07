# Python type hierarchy

# Lo siguiente es considerado un subconjunto de la jerarquía de tipos en python.

## Numbers

# Podemos dividir los números en python en dos secciones

# - Integral
#   - integers
#   - Boolean 
# - Non-Integral
#   - Floats (como doubles en C)
#   - Complex numbers (número que se expresa como la suma de un número real(ℝ) y un número imaginario (i). Un número imaginario es aquel cuyo cuadrado es negativo.)
#   - Decimal (representa numeros reales como float pero se diferencian en que podemos controlar la precisión es decir el número de decimales)
#   - Fractions (por ej 1/3 tiene infinitos decimales así q ni floats ni decimals pueden representarlos)

# ## Collections 

# Pueden ser divididas en:

# - Sequences
#   - Mutable 
#     - List
#   - Inmutable 
#     - Tuples 
#     - Strings 
# - Sets
#   - Mutable
#     - Sets
#   - Inmutables 
#     - Frozen sets
# - Mappings
#   - Dictionaries 

# ## Callables

# Algo que puedes invocar como una función.

# - User-defined Functions 
# - GEnerators 
# - Classes 
# - Instance methods
# - Class instances (__call__())
# - Built-in functions (len(), open())
# - Built-in Methods (myList.append(x))

# ## Singletons 

# - None 
# - NotImplemented 
# - Ellipsis operator (...)

# Multi-line statements and Strings

## multiline-statements

# A python program made by:

# 1. physical lines of code, which ends with physical newline character. It is turn into a...
# 2. logical lines of code, which ends with logical newline token. it is...
# 3. tokenized

# so when we write python code we can break line in implicit or explicit way:
#  - implicit, could be when we are using lists, tuples, dict,...
#  - explicit, we must use a back slash character '\' 

# implicit break line
my_list= [1, # it works 
          2,
          3
            ]

my_list
# explicit
 
# it is eligal

# if True 
#     and True:
#     print('hello')

if True \
    and True:
    print('hello')


## multiline strings

# To specify a multiline string we can use three quotes in a row.
# They are similar to a regular string but not because if u write a '\t' it will be kept into the string variable

my_multiple_line = ''' hello i am 
david!
'''
my_multiple_line

# Functions

# We have two ways to difine a function:

# - using def, must follow some rules
# - using lambda expression, must be in one line only (anonimous function)

# def 
def my_func():
   return 'david'

my_func

fn1 = lambda x,y : x**2+y
fn1
fn1(2,5)
l = [1,2,3]

val = 1

found = False
print(id(found))
idx = 0

while idx< len(l):
    
    if l[idx] == val:
        found = True
        print(id(found))
        break
    idx+=1
if not found:
    l.append(val) 

print(l)
0/10
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages = pages

    # magic methods
    def __str__(self):
        return f'{self.title} by {self.author} with {self.pages} pages'
    
    def __repr__(self):
        return f' book({self.title},{self.author},{self.pages})'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')
    
    def __eq__(self,other):

        if isinstance(other,Book):
            return self.author == other.author and self.title == other.title and self.pages == other.pages
        else:
            return False

    def __lt__(self,other): # less than, para saber si un libro es menor q otro usamos el número de páginas

        if isinstance(other,Book):
            return self.pages == other.pages
        else:
            return NotImplemented

b = Book('titulo1','autor1',100)
c = Book('titulo1','autor1',100)

c
b == c
class House:

    def __init__(self,price):
        self.price = price
    # price como variable privada, generamos sus set/get/del


# =============================================
    # definimos la property price y el getter
    @property
    def price(self):
        return self.price

# =============================================
    # setter method
    @price.setter
    def price(self,new_price):
        if new_price < 0 or not isinstance(float(new_price), float):
            raise ValueError("price cannot be negative and must be a float number")

        self._price = float(new_price)
# =============================================
    # deleter method
    @price.deleter
    def price(self):
        del self.price
h = House(100)

h


print(h.my_price)