import math as solve

class basic_calc:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    def sum(self):
        return self.val1+self.val2
    def subt(self):
        return self.val1-self.val2
    def div(self):
        return self.val1/self.val2
    def prod(self):
        return self.val1*self.val2
    def __str__(self):
        return (f"{self.val1} & {self.val2}")
