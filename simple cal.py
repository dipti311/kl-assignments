def add(operand1, operand2):
    return operand1+operand2
def subtract(operand1, operand2):
    return operand1 - operand2
def multiply(operand1, operand2):
    return operand1 * operand2
def divide(operand1, operand2):
    return operand1 / operand2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

user_choice = input("Enter choice(1/2/3/4): ")
if user_choice in ('1','2','3','4'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input please a number")

        
if user_choice=='1':
 print(num1,"+", num2,"=", add(num1, num2))

elif user_choice=='2':
        print(num1,"-", num2,"=", subtract(num1, num2))

elif user_choice=='3':
         print(num1, "*", num2,"=", multiply(num1, num2))
elif user_choice == '4':
        print(num1, "/", num2,"=", divide(num1, num2))

