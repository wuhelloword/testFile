class ClassMale:
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        # 如果想让一个对象成为可迭代对象，即可以使用for，那么必须实现__iter__方法
        return ClassItrator()




class ClassItrator:
    """被返回的对象"""
    def __iter__(self):
        pass

    def __next__(self):
        pass



if __name__ == '__main__':
    classmale = ClassMale()

    classmale.add('张三')
    classmale.add('李四')
    classmale.add('王五')


    for i in classmale:     # for循环，1.首先去判断classmale是否是可迭代对象，即判断classmale对象里是否有__iter__方法，2.判断这个方法中是否返回一个对象的引用，且被引用的对象中有__iter__方法和__next__方法，即，是一个迭代器。
        print(i)            # 满足上面的条件的话，



    # 如果要让类创建出来的实例对象可以使用for，在定义的类中添加__iter__方法
