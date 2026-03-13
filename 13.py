#Sum of Array Elements
n = int(input("Enter number of elements: "))
arr = []
sum = 0

for i in range(n):
    arr.append(int(input("Enter element: ")))

for i in arr:
    sum += i

print("Sum of elements:", sum)