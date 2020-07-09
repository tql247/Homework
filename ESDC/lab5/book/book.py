class Book:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def getName(self):
        return self.name

    def getId(self):
        return self.id
        
    def edit(self, name):
        self.name = name
    