def majorityelement(mylist):
    length = len(mylist)
    majority_ele = None
    counter = 0
    for i in range(length):
        if i==0:
            majority_ele = mylist[i]
            counter = 1
        elif mylist[i] == majority_ele:
            counter = counter + 1
        else:
            counter = counter - 1
        if counter == 0:
            majority_ele = mylist[i]
            counter = 1
    if counter>=1:
        count = 0
        for i in mylist:
            if i == majority_ele:
                count = count + 1
        if count >= length/2:
            return majority_ele
    return "no majority element"

mylist = [1, 3, 3, 3, 2, 1, 3,3]

print(majorityelement(mylist))



        
     