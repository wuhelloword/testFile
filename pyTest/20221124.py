class Fibonacci:
    """迭代器实现斐波那契数列"""
    def __init__(self, num):
        self.fbnc_list = list()
        self.i = 0
        self.a = 1
        self.b = 1
        self.num = num


    def __iter__(self):
        return self

    def __next__(self):


        if self.i == 0 or self.i == 1:
            self.i += 1
            return self.b

        if self.i < self.num:
            self.a, self.b = self.b, self.a+self.b
            self.i += 1
            return self.b
        else:
            raise StopIteration


if __name__ == '__main__':

    classmale = Fibonacci(12)

    for i in classmale:
        print(i)
