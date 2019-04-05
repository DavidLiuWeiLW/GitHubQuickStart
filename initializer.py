# encode: utf-8

import numpy as np
import math
from functools import reduce


class Initializer(object):
    """Initializer base class: all initializers inherit from this class.
    """

    def __call__(self):
        raise NotImplementedError

    def get_config(self):
        return {}


class Binary(Initializer):
    """二进制编码"""

    def __init__(self, lb=-1, ub=1, precision=4, length=10, size=100):

        # 检查precision值
        assert precision > 0, "`precision` must be not less than 0."
        assert lb <= ub, "`lb` must be no more than `ub`."

        super(Binary, self).__init__()
        self.lb = lb
        self.ub = ub
        self.precision = math.ceil(precision)
        self.length = length
        self.size = size
        self.bits = math.ceil(
            math.log2((ub - lb) * 10**math.ceil(precision) + 1))
        self.shape = (size, self.bits * length)
        self.solution = np.random.randint(0, 2, self.shape)

    def decode(self):
        def binary2int(l):
            return int(reduce(lambda x, y: str(x) + str(y), l), 2)

        def scale(n):
            return (((self.ub - self.lb) * 10**self.precision) / (2**self.bits - 1) * n) / 10**self.precision + self.lb

        return np.array(list(map(lambda item: [scale(binary2int(item[i * self.bits:(i + 1) * self.bits]))
                                               for i in range(0, self.length)], self.solution)))

    def get_config(self):
        return {
            'lb': self.lb,
            'ub': self.ub,
            'precision': self.precision,
            'length': self.length,
            'size': self.size,
            'bits': self.bits,
            'shape': self.shape
        }


class Permutation(Initializer):
    """docstring for permutation"""

    def __init__(self, arg):
        super(Permutation, self).__init__()


if __name__ == '__main__':
    s = Binary()
    print(s.get_config())
