class myclass():
    def __init__(self, x):
        self.x = x
        
    def calc_1(self):
        try:
            if self.x <= 1.707 or self.x >= 52.868:
                return self.x ** 4 * 1.798 + self.x ** 3 * 4.341 - self.x ** 2 * 5.205 + self.x * 4.848
        except TypeError:
            return "Error"

    def calc_2(self):
        try:
            if self.x <= 1.707 or self.x >= 52.868:
                return self.x ** 3 * 6.955 - self.x ** 2 * 3.268 + self.x * 8.392
        except TypeError:
            return "Error"

    def calc_3(self):
        try:
            if self.x <= 1.707 or self.x >= 52.868:
                return self.x ** 2 * 4.078 + self.x * 2.614
        except TypeError:
            return "Error"

    def calc_4(self):
        try:
            if self.x <= 1.707 or self.x >= 52.868:
                return self.x * 5.632
        except TypeError:
            return "Error"

if __name__ == '__main__':
    x = float(input("input float: "))
    m = myclass(x)
    print(m.calc_1())
    print(m.calc_2())
    print(m.calc_3())
    print(m.calc_4())
