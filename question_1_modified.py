from random import randint

def fun(n):
    luck = 0
    dice = randint(1,6)
    if dice == 6:
        luck = 1

    if n == 1:
        return 1, luck
    elif n == 2:
        return 2, luck
    else:
        y_n1, luck_n1 = fun(n- 1)       # only one recursive call
        # compute y_n2 and luck_n2 iteratively instead of recursion
        if n - 2 == 1:
            y_n2, luck_n2 = 1, 0
        else:
            y_n2, luck_n2 = 2, 0

        y = y_n1 + 2*y_n2
        luck += luck_n1 + luck_n2
        return y, luck

print(fun(4))