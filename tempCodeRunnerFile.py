numbers = [1,2,2,3,4,5,5,4,4,6,8,8,9,9,9]
newlist=[] #new empty list
for i in range (len(numbers)):
    if numbers[i] not in newlist :
        newlist.append(numbers[i])
print ("The unique values are: ", newlist)