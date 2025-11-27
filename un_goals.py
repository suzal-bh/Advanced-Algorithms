
def SelectUNGoals(student_id):

    # total is the sum of all the numbers
    # this is our first number
    total = 0
    for n in str(student_id):
        total += int(n)
    
    #last_two is the last two digits of the id
    # this is our second number
    last_two = int(str(student_id)[-2:])
    product = (last_two // 10) * (last_two % 10)

    #this calc bring the numbers in the range of 1-17
    goal_1 = (total % 17) + 1
    goal_2 = (product % 17) + 1


    # this makes sure that both the numbers are different
    if goal_1 == goal_2:
        goal_2 = (goal_2 % 17) + 1

    return goal_1, goal_2


print(SelectUNGoals(123842))