# test builtin property

# create a property object explicitly
property()
property(1, 2, 3)

# use its accessor methods
p = property()
p.getter(1)
p.setter(2)
p.deleter(3)

# basic use as a decorator
class A:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("x get")
        return self._x

a = A(1)
print(a.x)

try:
    a.x = 2
except AttributeError:
    print("AttributeError")

# explicit use within a class
class B:
    def __init__(self, x):
        self._x = x

    def xget(self):
        print("x get")
        return self._x

    def xset(self, value):
        print("x set")
        self._x = value

    def xdel(self):
        print("x del")

    x = property(xget, xset, xdel)

b = B(3)
print(b.x)
b.x = 4
print(b.x)
del b.x

# full use as a decorator
class C:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("x get")
        return self._x

    @x.setter
    def x(self, value):
        print("x set")
        self._x = value

    @x.deleter
    def x(self):
        print("x del")

c = C(5)
print(c.x)
c.x = 6
print(c.x)
del c.x
