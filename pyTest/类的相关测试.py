# class Employee():
#     __class_version = "v1.0"
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     @classmethod
#     def cls_ver_get(cls):
#       return cls.__class_version
#
#     @classmethod
#     def cls_ver_set(cls, new_version):
#       cls.__class_version = new_version


# print(Employee.cls_ver_get())
# Employee.cls_ver_set("v1.1")
# print(Employee.cls_ver_get()


class Employee():
    __class_version = "v1.0"
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def cls_ver_get(cls):
        return cls.__class_version

worker0 = Employee(0, "John")

# worker0.say_name() 动态方法未绑定报错
# print(worker0.class_version) 动态属性未绑定会报错
def say_name(self):
    print("My name is %s" % self.name)
Employee.say_name = say_name
Employee.class_version = "v1.0"
#
worker0.say_name()
print(worker0.class_version)


