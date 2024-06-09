from queue import LifoQueue

class Queue:
    def __init__(self):
        self.s1 = LifoQueue()
        self.s2 = LifoQueue()
        
    def enqueue(self, value):
        # add element
        self.s1.put(value)
        pass

    def dequeue(self):
        # Pop top element - do not return
        if self.isEmpty():
            return None
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.put(self.s1.get())
        return self.s2.get()
        pass

    def peek(self):
        # return top element
        if self.isEmpty():
           
            return None
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.put(self.s1.get())
        
        # Return the top element from s2 without popping it
        return self.s2.queue[-1]
        pass

    def isEmpty(self):
        # return boolean value if empty
        return self.s1.empty() and self.s2.empty()
        pass

