      def input_number():
 N=input()
 NUM=N.split(' ')
 return NUM[0],NUM[1],NUM[2]

      def compare(a, b, c):
if (b >= a) and (b >= c): 
return b
elif (a >= b) and (a >= c):
return a
else: return c

      def display(a, b, c, greatest): 
 print('{0} is the greatest number among {1},{2} and {3}'.format(greatest,a,b,c)) 
def main(): 
Num1,Num2,Num3 = input_number() 
greatest_num = compare(Num1, Num2, Num3) 
display(n1, n2, n3, greatest_num)
      main()
