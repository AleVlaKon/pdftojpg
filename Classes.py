# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def is_triangle(self):
        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1

        if self.a + self.b < self.c or self.b + self.c < self.a or self.a + self.c < self.b:
            return 2
        else:
            return 3




tr = TriangleChecker(3, 4, 5)
print(tr.is_triangle())