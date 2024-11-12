class VAR:
    '''VAR(name) == name'''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)
    
    def __repr__(self):
        return "VAR({})".format(str(self.name))
    
    def comma_format(self):
        return str(self.name)
    
    def evaluate(self, assignment):
        return assignment[self.name]
    
    def __eq__(self, other):
        return isinstance(other, VAR) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __len__(self):
        return 1
