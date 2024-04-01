class var:
    class int:
        def __init__(self, value):
            self.value = int(value)

        def __str__(self):
            return f"{self.value}"
        
    class float:
        def __init__(self, value):
            self.value = float(value)

        def __str__(self):
            return f"{self.value}"
        
    class complex:
        def __init__(self, real, imag):
            self.value = complex(real, imag)

        def __str__(self):
            return f"{self.value}"
    
    class str:
        def __init__(self, value):
            self.value = str(value)

        def __str__(self):
            return f"{self.value}"
        
    class bool:
        def __init__(self, value):
            self.value = bool(value)

        def __str__(self):
            return f"{self.value}"
    class list:
        def __init__(self, iterable):
            self.value = list(iterable)

        def __str__(self):
            return f"{self.value}"
    
    class dict:
        def __init__(self, **kwargs):
            self.value = kwargs

        def __str__(self):
            return str(self.value)