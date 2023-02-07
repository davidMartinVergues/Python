def run ():
    for num in range(101):
        if is_primary(num):
            print(num)



def is_primary(num):

    if num == 0 or num == 1:
        return False

    for x in range(2,num):
        if x != num and num%x == 0:
            return False
    return True
    



if __name__ == "__main__":
    run()
