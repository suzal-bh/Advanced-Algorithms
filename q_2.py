pairs = [
    [5, "B"], [8, "O"], [14, "Si"], [16, "S"], 
    [19, "K"], [29, "Cu"], [47, "Ag"], [72, "Hf"], [92, "U"]
]

def fun(pairs, k):
    left = 0
    right = len(pairs) - 1

    while left <= right:
        mid = (left + right) // 2

        if pairs[mid][0] == k:
            return pairs[mid][1]
        
        if pairs[mid][0] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(fun(pairs, k = 14))
