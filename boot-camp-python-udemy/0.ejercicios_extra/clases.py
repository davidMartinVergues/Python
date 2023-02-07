class Sample:
    def __init__(self,name='anonimo', age= 0):
        self.__name = name # mangling
        self.__age = age  # mangling
    def greet(self):
        return f'hello! my name is {self.__name} an i am {self.__age}'

s1 = Sample('david',10)



#s1._Sample__name = 'ffff'

#s1.__name = 'ffff'
print(s1)
# 'hello! my name is david an i am 10'



# s1._Sample__name = 'ffff'

# property decorator


class House:

    def __init__(self,price):
        self._price = price
    # price como variable privada, generamos sus set/get/del


# =============================================
    # definimos la property price y el getter
    @property
    def price(self):
        return self._price
    
# =============================================
    #setter method
    @price.setter
    def price(self,new_price):
        if new_price < 0 or not isinstance(float(new_price), float):
            raise ValueError("price cannot be negative and must be a float number")

        self._price = float(new_price)
# =============================================
    # deleter method
    @price.deleter
    def price(self):
        del self._price

my_house = House(100)


print(my_house.price) # 100

try:
    my_house.price = -200
finally:
    print(my_house.price) # 100

