import pandas
from datetime import timezone
import import_me


# df = pandas.DataFrame([1,2])

# print('¡this is a module')

# print(__name__) # __main__

# print(pandas.__name__) #  pandas

# print(timezone.__name__) #  timezone en este caso timezone es una función de datetime pero es considerado el módulo por lo q le da su nombre a la variable __name__


if __name__ == '__main__':
    df = pandas.DataFrame([1,2])

    print('¡this is a module')

    print(__name__) # __main__

    print(pandas.__name__) #  pandas

    print(timezone.__name__) #  timezone en este caso timezone es una función de datetime pero es considerado el módulo por lo q le da su nombre a la variable __name__
