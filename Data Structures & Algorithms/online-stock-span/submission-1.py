class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        i = len(self.stock) - 2
        while i >= 0 and self.stock[i] <= price:
            i -= 1
        return len(self.stock) - i - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)