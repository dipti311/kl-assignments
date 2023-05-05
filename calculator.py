class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def substract(self):
        print(self.a-self.b)
    def multiply(self):
        print(self.a*self.b)
    def divide(self):
        print(self.a/self.b)
user_choice=int(input())
a=int(input())
b=int(input())
user=Calculator(a,b)






