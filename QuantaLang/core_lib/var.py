import json

interpretationFile = open("ipt.json", "a")
with open('ipt.json', 'r') as f:
    try:
        data = json.load(f)
    except ValueError:
        data = []


def call_method(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        new_data = {
            "variable": self.variable,
            "value": self.value,
            "type": type(self.value).__name__
        }
        self.dump_data(new_data)  # Call the method here
        return result
    return wrapper

class Meta(type):
    def __init__(cls, name, bases, attrs):
        attrs['common_method'] = lambda self: print("This is a common method")
        super().__init__(name, bases, attrs)

class Deposit(metaclass=Meta):
    def __init__(self):
        pass

    def dump_data(self, new_data):
        with open('ipt.json', 'r') as f:
            try:
                data = json.load(f)
            except ValueError:
                data = []
        data.append(new_data)
        with open('ipt.json', 'w') as f:
            json.dump(data, f)


class var:
    class int(Deposit):
        @call_method
        def __init__(self,variable, value):
            self.variable = variable
            self.value = int(value)
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "int"
            }
            data.append(new_data)
        def __str__(self):
            return f"{self.value}"
        
    class float(Deposit):
        @call_method
        def __init__(self,variable, value):
            self.variable = variable
            self.value = float(value)

        def __str__(self):
            return f"{self.value}"
        
    class complex(Deposit):
        @call_method
        def __init__(self,variable, real, imag):
            self.variable = variable
            self.value = complex(real, imag)
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "complex"
            }
            data.append(new_data)

        def __str__(self):
            return f"{self.value}"
    
    class str(Deposit):
        @call_method
        def __init__(self,variable, value):
            self.variable = variable
            self.value = str(value)
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "str"
            }
            data.append(new_data)
        def __str__(self):
            return f"{self.value}"
        
    class bool(Deposit):
        @call_method
        def __init__(self,variable, value):
            self.variable = variable
            self.value = bool(value)
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "bool"
            }
            data.append(new_data)
        def __str__(self):
            return f"{self.value}"
    class list(Deposit):
        @call_method
        def __init__(self,variable, iterable):
            self.variable = variable
            self.value = list(iterable)
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "list"
            }
            data.append(new_data)

        def __str__(self):
            return f"{self.value}"
    
    class dict(Deposit):
        @call_method
        def __init__(self,variable, **kwargs):
            self.variable = variable
            self.value = kwargs
            new_data = {
                "variable": self.variable,
                "value": self.value,
                "type": "dict"
            }
            data.append(new_data)

        def __str__(self):
            return str(self.value)


   

print(var.bool("tf", True))