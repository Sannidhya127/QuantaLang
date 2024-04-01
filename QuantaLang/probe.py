class probe:
    class Probe:
        def __init__(self, value):
            self.value = value
        
        def __str__(self): 
            return str(self.value)
    
    class sum:
        def __init__(self, *args):
            self.value = sum(args)
        
        def __str__(self) -> str:
            return str(self.value)
        
    class sub:
        def __init__(self, *args):
            self.value = args[0] - sum(args[1:])

        def __str__(self) -> str:
            return str(self.value)