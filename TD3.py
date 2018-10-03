class Naturel:
    def __init__ (self,x):
        if type(x) == type(1) and x >= 0:
            self.x = x
        else:
            raise TypeError('Type is not an int')

    def add(self, *args):
        for i in args:
            if type(i) != type(1) and i >= 0:
                raise TypeError('Arguments type are not naturals number')
                return None
        for i in args:
            self.x += i
        return self.x

    def cmp(self, y):
        if type(y) != type(1) and y >= 0:
            raise TypeError('Type is not an int')
            return None
        if self.x > y:
            return 1
        elif self.x < y:
            return -1
        return 0

class Rationnel:
    def __init__(self,x):
        if type(x) == type(-1):
            self.x = x
        else:
            raise TypeError('Bad argument type')
        
    def add(self, *args):
        for i in args:
            if type(i) != type(-1):
                raise TypeError('Bad argument type at %d' % (i))
                return None
        for i in args:
            self.x += i
        return self.x

     def cmp(self, y):
        if type(y) != type(1):
            raise TypeError('Type is not a rationnal')
            return None
        if self.x > y:
            return 1
        elif self.x < y:
            return -1
        return 0
