numList = []

number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    numList.append(value)

numList.sort()

print("Element After Sorting List in Ascending Order is : ", numList)