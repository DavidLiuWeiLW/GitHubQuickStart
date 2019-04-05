
class obj_parent(object):
    """docstring for obj_test"""

    def __init__(self, arg):
        self.arg = arg

    def __call__(self):
        print("An instance is called!")


class obj_child(obj_parent):
    """docstring for obj_child"""

    def __init__(self, arg):
        super(obj_child, self).__init__(arg)
        self.arg = arg

    def __call__(self):
        print("An child instance is called!")


if __name__ == '__main__':
    child_instance = obj_child(1)
    child_instance()

    parent_instance = obj_parent(2)
    parent_instance()
