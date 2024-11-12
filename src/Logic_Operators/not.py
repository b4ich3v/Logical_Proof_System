class NOT:
    '''NOT(expression) == (!expression)'''
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        if isinstance(self.expression, VAR) or isinstance(self.expression, NOT):
            return "!{}".format(str(self.expression))
        elif isinstance(self.expression, bool):
            return "!({})".format(str(self.expression))
        else:
            return "!({})".format(str(self.expression))
    
    def __repr__(self):
        return "NOT({})".format(repr(self.expression))
    
    def comma_format(self):
        return "(!{})".format(self.expression.comma_format())
    
    def evaluate(self, assignment):
        return not self.expression.evaluate(assignment)
    
    def __eq__(self, other):
        return isinstance(other, NOT) and self.expression == other.expression
    
    def __hash__(self):
        return hash(self.expression)
    
    def __len__(self):
        if isinstance(self.expression, bool):
            return 2
        else:
            return len(self.expression) + 1
