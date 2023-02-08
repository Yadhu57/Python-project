class rectangle:
    def area(self, l, b):
        print('Area of rectangle is:', l * b)


class square(rectangle):
    def area(self, l, b):
        print('Area of square is:', l * b)


ob = square()
ob.area(10, 20)

