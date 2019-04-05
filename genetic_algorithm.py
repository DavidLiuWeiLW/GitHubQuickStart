
from initializer import *


class GeneticBinary(Binary):
    """docstring for GeneticBinary"""

    def __init__(self, lb=-1, ub=1, precision=4, length=10, size=100):
        super(GeneticBinary, self).__init__(lb, ub, precision, length, size)
        self.obj_value = None

    def getObjectFuncValue(self, object_func):
        self.obj_value = np.array(
            list(map(lambda x: object_func(x), self.decode())))
        return self.obj_value


def CrossOver():
    pass


def Selection():
    pass


def Mutation():
    pass


def test_func(a):
    print(a)


def call_func(test_func, a):
    test_func(a)


def obj(args):
    return sum(list(map(lambda x: x**2, args)))


if __name__ == '__main__':
    S = GeneticBinary(lb=-2, ub=2)
    call_func(test_func, S.get_config())
    print(len(S.getObjectFuncValue(obj)))
