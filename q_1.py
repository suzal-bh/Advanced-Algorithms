#Q_1: with 2 recursive calls
from random import randint

def fun(n):
    luck = 0
    #roll a dice randomly 
    dice = randint(1, 6)

    if dice == 6:
        luck = 1
    
    if n == 1:
        y = 1
    elif n == 2:
        y = 2
    else:
        # compute fun(n-1) and fun(n-2)
        first_result = fun(n - 1)
        second_result = fun(n - 2)

        first_entry, first_luck = first_result
        second_entry, second_luck = second_result

        y = first_entry + 2 * second_entry

        #add all the luck values
        luck += first_luck + second_luck
    
    #return the result as a tuple
    return y, luck

print(fun(4))


# Q_1: with only one recursive call
def fun(n):
    luck = 0
    #roll a dice randomly 
    dice = randint(1, 6)
    
    if dice == 6:
        luck = 1
    
    if n == 1:
        return 1, 0, luck
    if n == 2:
        return 2, 1, luck
    
    #only one recursive call
    first_result = fun(n - 1)
    
    first_entry, second_entry, first_luck = first_result

    y = first_entry + 2 * second_entry

    luck += first_luck 

    #return the result as a tuples
    return y, first_entry, luck

result = fun(4)
print(result[0], result[2])

