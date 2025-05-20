import random
class MonteCarlo:
    def __init__(self,function,a: int,b: int):
        self.function= function
        self.a= a
        self.b= b
    
    def integrate(self,N):
        sumfunction=0
        for i in range(N):
            x=random.uniform(self.a,self.b)
            sumfunction+= self.function(x)
        result= (self.b - self.a)/N * sumfunction
        return result
    
monte_carlo_for_x_squared= MonteCarlo(lambda x:x**2 , 0,5)
print(monte_carlo_for_x_squared.integrate(1000))