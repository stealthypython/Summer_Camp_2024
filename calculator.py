numOne = int(input("enter first number: "))
numTwo = int(input("enter second number:"))
print("numbers: ", numOne, "and", numTwo)
print("operations")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("finally, / for division [cannnot divide by zero]")
operation = input("Enter operation: ")
if operation == "+":
  print(numOne, "+", numTwo, "=", numOne + numTwo)
elif operation == "-":
  print(numOne, "-", numTwo, "=", numOne - numTwo)
elif operation == "*":
  print(numOne, "*", numTwo, "=", numOne * numTwo)
elif operation == "/":
 if numTwo != 0:
  print(numOne, "/", numTwo, "=", numOne / numTwo)
else:
  print("cannot divide by zero.. try again!")
