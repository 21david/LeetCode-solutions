class RecentCounter:
    def __init__(self):
        self.deque = deque()

    # O(1) due to constant 3000 upper bound
    def ping(self, t: int) -> int:
        self.deque.append(t)

        while self.deque[0] < t - 3000:
            self.deque.popleft()

        return len(self.deque)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
