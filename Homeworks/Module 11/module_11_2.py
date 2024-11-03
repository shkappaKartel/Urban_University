def introspection_info(obj):

    obj_type = type(obj)
    obj_module = obj_type.__module__
    obj_dir = dir(obj)
    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in obj_dir if callable(getattr(obj, method)) and not method.startswith('__')]


    info = {
        'tpye': obj_type.__name__,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods
    }

    return info


class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

my_obj = MyClass(10)

info = introspection_info(my_obj)
print(info)