class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = self.capacity * [0]
        self.length = 0

    def get(self, i: int) -> int:
        if i < self.length:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
            return self.array[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = self.capacity * [0]

        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity