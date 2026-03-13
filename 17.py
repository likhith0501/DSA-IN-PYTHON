##Queue Implementation


##Concept: Queue follows FIFO (First In First Out).

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        print("Queue:", self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()
print("Removed:", q.dequeue())
q.display()