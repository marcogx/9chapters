# implemented with circular-array


class Queue:

    def __init__(self):
        self.array = [0] * 1
        self.first = 0  # index of head
        self.last = 0  # index of next available slot 
        self.size = 0
        
    def resize(self, new_len):
        new_arr = [0] * new_len
        for i in xrange(self.size):
            new_arr = self.array[(self.first + i) % len(self.array)]
        self.array = new_arr
        self.first = 0
        self.last = self.size
        
    def push(self, element):
        if self.size == len(self.array):
            self.resize(2 * len(self.array))
        self.array[self.last] = element
        self.last += 1
        if self.last == len(self.array):
            self.last = 0
        self.size += 1
            
    def top(self):
        if self.size == 0:
            raise ValueError('top from empty queue')
        return self.array[self.first]

    def pop(self):
        if self.size == 0:
            raise ValueError('pop from empty queue')
        rtn = self.array[self.first]
        self.first += 1
        self.size -= 1
        if self.first == len(self.array):
            self.first = 0
        if self.size > 0 and self.size == len(self.array) / 4:
            self.resize(len(self.array) / 2)
        return rtn

q = Queue()
q.push(1)
print q.pop()