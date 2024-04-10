class Tokenize:
    def __init__(self,token):
        self.token = token

    def tokenize(self):
        return self.token.split()
    
    def __str__(self):
        return f"{self.token}"
    
    def get_position(self, item):
        return self.token.split().index(item)


