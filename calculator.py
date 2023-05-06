'''class Calculator:
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
    def take_input():
        user_choice=int(input())
        a=int(input())
        b=int(input())
        return


'''
class Calculator:
    """A basic calculator class that performs arithmetic operations by using switch"""

    def __init__(self):
        self.input_1 = None
        self.input_2 = None

    def get_input(self):
        """Prompts the user to enter two numbers"""
        try:
            self.input_1 = float(input("Enter the first number: "))
            self.input_2 = float(input("Enter the second number: "))
            self.operator = input("Enter an operator (+, -, *, /): ")
        except ValueError:
            print("Invalid input")
            self.get_input()

    def add(self):
        """Adds the input_1 and input_2 values"""
        return self.input_1 + self.input_2

    def subtract(self):
        """Subtracts the input_2 value from the input_1 value"""
        return self.input_1 - self.input_2

    def multiply(self):
        """Multiplies the input_1 and input_2 values"""
        return self.input_1 * self.input_2

    def divide(self):
        """Divides the x value by the y value"""
        return self.input_1 / self.input_2

    def calculate(self):
        """Performs the specified arithmetic operation on the input_1 and input_2 values"""
        switcher = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

        operation = switcher.get(self.operator)
        if not operation:
            return "Invalid operator"

        if self.input_1 is None or self.input_2 is None:
            self.get_input()

        return operation()
# Created a new calculator object
calculator = Calculator()

# To take the inputs from user by get_input function
calculator.get_input()

# Perform a calculation
result = calculator.calculate()
# Prints the result
print(result)


