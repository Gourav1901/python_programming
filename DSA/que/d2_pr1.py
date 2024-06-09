from queue import Queue

class Stack:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()
    
    def push(self, value):
        # Write code to push value
        self.Q2.put(value)
        while not self.Q1.empty():
            self.Q2.put(self.Q1.get())
        self.Q1,self.Q2 = self.Q2,self.Q1
        pass
    
    def pop(self):
        # write code to pop and print poped value
        if self.Q1.empty():
            print("Stack is empty")
            return None
        # Dequeue from Q1
        pop_value = self.Q1.get()
        print(pop_value)
        return pop_value
        pass

    def top(self):
        # write code to print top value
        if self.Q1.empty():
            print("Stack is empty")
            return None
        # The front element of Q1 is the top element
        top_value = self.Q1.queue[0]  # Directly access the internal deque of the queue
        print(top_value)
        return top_value
        pass

    def isEmpty(self):
        # return boolean value
        return self.Q1.empty()
        pass


