class Math:
    def num(self, a, b):
        self.x = a
        self.y = b

    def sum(self):
        print("sum = ", self.x + self.y)

    def product(c):
        print("product = ", c.x * c.y)


obj = Math()
obj.num(10, 5)
obj.sum()
obj.product()

