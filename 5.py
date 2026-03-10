## Queue using List
queue = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    queue.append(x)

print("Queue:", queue)

print("Dequeued element:", queue.pop(0))
print("Queue after dequeue:", queue)