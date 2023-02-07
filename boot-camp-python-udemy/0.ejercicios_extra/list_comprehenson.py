

def run ():

    list1 = [[1,2,3],[4,5,6],[7,8,9]]
    list2 = [val for sublist in list1 for val in sublist]

    print(list2)
    list_generator(100000)

def list_generator(num):
    return [num for num in range(1,num) if num%4==0 and num%6==0 and num%9==0]


if __name__ == "__main__":
    run()