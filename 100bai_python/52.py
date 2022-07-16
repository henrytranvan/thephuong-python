class Circle(object): 
    def __init__(self, r): 
        self.radius = r 
        # Bài Python 52, Code by Quantrimang.com 
    def area(self): 
        return self.radius**2*3.14 
    
aCircle = Circle(2) 
print (aCircle.area())