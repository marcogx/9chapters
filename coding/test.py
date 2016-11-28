a = 1


def fun(a):
    print "fun_in", id(a)
    a = 2
    print "re-point", id(a), id(2)


def foo(x):
    print "executing foo(%s)" % x


class A(object):

    class_var = 100

    def __init__(self, v1):
        self.v1 = v1

    def foo(self, x):
        print "executing foo(%s,%s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        cls.class_var += 1
        print "executing class_foo(%s,%s)" % (cls, x)

    def static_foo(x):
        print "executing static_foo(%s)" % x


# a1 = A(99)
# a2 = A(88)

# print a1.v1
# print a1.class_var
# a1.class_foo(0)
# print a1.class_var
# print a2.class_var
# a1.class_var = 0
# print a1.class_var
# print a2.class_var
# print A.class_var
#
# print a1.__dict__
# print a2.__dict__
# print dir(a1)
# print dir(a2)

# name = 'Guang'
# name = [1, 2, 3]
# print 'hi there %s' % (name, )

# arr = '1 2 3 4'
# arr = map(int, arr.split())
# print arr

# a, b = [1, 2]
# print a
# print b + 9

sz = 10
for i in xrange(sz):
    print i
    print 'sz', sz
    sz -= 3