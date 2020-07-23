operand1 = int(input("Enter the first number: "))
operand2 = int(input("Enter the second number: "))
operator  = input("Enter the operator " + '+,/,*,-: = ')
if operand1 == 45 and operand2 ==3 and operator == '*':
    print("555")
elif operand1 ==56 and operand2 == 9 and operator == '+':
    print("77")
elif operand1 ==56 and operand2 == 6 and operator =='/':
    print("4")
elif operator == '+':
    num1 = operand1+ operand2
    print(num1)
elif operator == '*':
    num1 = operand1 * operand2
    print(num1)
elif operator == '-':
    num1 = operand1 - operand2
    print(num1)
elif operator == '/':
    num1 = operand1/ operand2
    print(num1)


