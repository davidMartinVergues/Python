
import math

def run ():
    print(dic_generator(10))


def dic_generator(num):
    return {num:round(math.sqrt(num),5) for num in range(1,num)}



if __name__ == "__main__":
    run()