from random import randint

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




