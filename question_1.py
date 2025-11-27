from random import randint

def fun(n):
    luck = 0
    dice = randint(1, 6)

    if dice == 6:
        luck = 1
    
    if n == 1:
        y = 1
    elif n == 2:
        y = 2
    else:
        #recursion call for n - 1
        y_n1, luck_n1 = fun(n - 1)

        #recursion call for n - 2
        y_n2, luck_n2 = fun(n - 2)

        #compute y
        y = y_n1 + 2 * y_n2
        
        #add all the luck values
        luck += luck_n1 + luck_n2

    return y, luck

print(fun(4))