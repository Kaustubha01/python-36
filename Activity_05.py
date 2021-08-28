List1 = []

Number = 5
for i in range(1, Number+1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List1.append(value)

total = sum(List1)

print("\n The Sum of All Element in this List is : ", total)
