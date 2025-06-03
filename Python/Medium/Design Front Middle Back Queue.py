class FrontMiddleBackQueue:
    def __init__(self):
        self.first = deque()
        self.last = deque()
        self.size = 0

    # ------------------- PUSH ------------------- #
    def pushFront(self, val: int) -> None:
        if self.size % 2 == 0:
            self.first.appendleft(val)
        else: 
            self.last.appendleft(self.first.pop())
            self.first.appendleft(val)

        self.size += 1
        
    def pushMiddle(self, val: int) -> None:
        if self.size % 2 == 0:
            self.first.append(val)
        else: 
            self.last.appendleft(self.first.pop())
            self.first.append(val)

        self.size += 1
        
    def pushBack(self, val: int) -> None:
        if self.size == 0:
            # Exception: If this is the first val, then it will go into first instead of last
            self.first.append(val)
            self.size += 1
            return

        if self.size % 2 == 0:
            self.first.append(self.last.popleft())
            self.last.append(val)
        else:
            self.last.append(val)
        
        self.size += 1

    # ------------------- POP ------------------- #
    def popFront(self) -> int:
        if self.size == 0:
            return -1

        if self.size % 2 == 0:
            self.size -= 1
            self.first.append(self.last.popleft())
            return self.first.popleft()
        else:
            self.size -= 1
            return self.first.popleft()
        
    def popMiddle(self) -> int:
        if self.size == 0:
            return -1

        if self.size % 2 == 0:
            self.size -= 1
            middle = self.first.pop()
            self.first.append(self.last.popleft())
            return middle
        else:
            self.size -= 1
            return self.first.pop()
        
    def popBack(self) -> int:
        if self.size == 0:
            return -1

        if self.size % 2 == 0:
            self.size -= 1
            return self.last.pop()
        else:
            self.size -= 1
            self.last.appendleft(self.first.pop())
            return self.last.pop()
        
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# Used 2 hints
