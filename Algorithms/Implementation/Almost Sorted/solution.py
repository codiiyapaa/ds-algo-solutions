input()
array = [int(x) for x in input().split(" ")]

sorted_array = sorted(array)

if array == sorted_array:
    print("yes")
else:    
    wrong = []
    for i, (a, b) in enumerate(zip(array, sorted_array)):
        if a != b:
            wrong.append(i)
        if len(wrong) > 2:
            break