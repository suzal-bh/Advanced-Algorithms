pairs = [
    [5, "B"], [8, "O"], [14, "Si"], [16, "S"], 
    [19, "K"], [29, "Cu"], [47, "Ag"], [72, "Hf"], [92, "U"]
]

def fun(pairs, k):
    #start and end of the search interval
    left = 0
    right = len(pairs) - 1

    while left <= right:
        mid = (left + right) // 2

        #if the key is found, return to its associated value
        if pairs[mid][0] == k:
            return pairs[mid][1]
        
        #if the found key is larger than the mid key, move the left boundry to the right half
        if pairs[mid][0] < k:
            left = mid + 1
        #otherwise, the key must be in the left half
        else:
            right = mid - 1
    #if loop finishes wtiht no keys, return -1
    return -1

#looking for key 14
print(fun(pairs, k = 14))
