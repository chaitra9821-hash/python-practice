num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("Choose an operator:")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
choice=input("Enter your choice(+,-,%,/):")
if choice=="+":
  print("Result:",num1+num2)
elif choice=="-":
  print("Result:",num1-num2)
elif choice=="*":
  print("Result:",num1*num2)
elif choice=="/":
  if num!=0:
  print("Result:",num1/num2)
  else:
       print("Division by zero is not allowed.")
else:
    print("Invalid choice")

