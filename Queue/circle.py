class Queue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear+1) % self.k) == self.front:
            print("its is full buddy")
        elif self.rear == -1:
            self.rear = self.front = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Its Empty!")
        elif self.front == 0:
            self.queue[self.front] = None
            self.front += 1
        else:
            self.queue[self.front] = None
            self.front += 1

    def peek(self):
        print(self.queue)


q = Queue(5)

q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.dequeue()
q.dequeue()
q.dequeue()

q.enqueue(0)
q.enqueue(1)
q.enqueue(2)

q.peek()
