def input_number(): 
number1= int(input("Enter the first number"))
number2= int(input("Enter the second number"))
return number1, number2

def add(a,b):
return(a+b)

def display(a, b, c):
	print(f”{a} + {b} = {c}”)

def main():
number1, number2 = input_number()
answer= add(number1,number2)
display(number1,number2,answer)
main()
