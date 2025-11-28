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
        first_result = fun(n - 1)
        second_result = fun(n - 2)

        first_entry, first_luck = first_result
        second_entry, second_luck = second_result

        y = first_entry + 2 * second_entry

        luck += first_luck + second_luck

    return y, luck

print(fun(4))




