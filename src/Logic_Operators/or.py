class OR:
    '''OR(left, right) == (left | right)'''
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        if isinstance(self.left, VAR) or isinstance(self.left, bool) or isinstance(self.left, NOT) and isinstance(self.right, bool) or isinstance(self.right, VAR) or isinstance(self.right, NOT):
            return "{} | {}".format(str(self.left), str(self.right))
        elif isinstance(self.left, VAR) or isinstance(self.left, bool):
            return "{} | ({})".format(str(self.left), str(self.right))
        elif isinstance(self.right, VAR or isinstance(self.right, bool)):
            return "({}) | {}".format(str(self.left), str(self.right))
        else:
            return "({}) | ({})".format(str(self.left), str(self.right))
    
    def __repr__(self):
        return "OR({}, {})".format(repr(self.left), repr(self.right))
    
    def comma_format(self):
        return "({} | {})".format(self.left.comma_format(), self.right.comma_format())
    
    def evaluate(self, assignment):
        return self.left.evaluate(assignment) or self.right.evaluate(assignment)

    def __eq__(self, other):
        return isinstance(other, OR) and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        return hash((self.left, self.right))
    
    def __len__(self):
        if isinstance(self.left, bool) and isinstance(self.right, bool):
            return 3
        elif isinstance(self.left, bool):
            return len(self.right) + 2
        elif isinstance(self.right, bool):
            return len(self.left) + 2
        else:
            return len(self.left) + len(self.right) + 1
