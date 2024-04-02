# 在多个类中实现了同名的方法，他们的继承顺序称为方法解释顺序MRO，python2.3版本后采用C3线性序列算法来计算MRO
# 类之间的继承关系可以用有向无环图来描述，每个顶点代表一个类，顶点之间的有向边代表类之间的继承关系。
# C3算法对所有顶点进行线性排序。

class A(object):
    def f0(self):
        print('A f0')

    def f1(self):
        print('A f1')

class B(object):
    def f0(self):
        print('B f0')

    def f1(self):
        print('B f1')

class C(B):
    def f0(self):
        print('C f0')

class D(A, B):
    def f1(self):
        print('D f1')

class E(D, B):
    pass

class F(E, C, B):
    pass

print(F.__mro__)
f = F()
f.f0()
f.f1()
