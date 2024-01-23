class Queue:
    queue = []
    capacity = 5

    def IsEmpty(self):
        return len(self.queue) == 0

    def IsFull(self):
        return len(self.queue) == self.capacity

    def Enqueue(self, element):
        if self.IsFull():
            print("Queue is full, delete element first")
            return
        self.queue.append(element)

    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is already empty")
            return
        self.queue.pop(0)

    def Show(self):
        for element in self.queue:
            print(element)

queue = Queue()

while True:
    desired_op = int(input("Indicate number of desired operation. (1 = IsEmpty, 2 = IsFull, 3 = Enqueue, 4 = Dequeue, 5 = Show elements):"))
    if desired_op == 1:
        print(f"Queue is {'not' if not queue.IsEmpty() else ''} empty")
    elif desired_op == 2:
        print(f"Queue is {'not' if not queue.IsFull() else ''} full")
    elif desired_op == 3:
        element = input("Input element:")
        queue.Enqueue(element)
        queue.Show()
    elif desired_op == 4:
        queue.Dequeue()
        queue.Show()
    elif desired_op == 5:
        queue.Show()







