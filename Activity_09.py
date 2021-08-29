l=float(input("Enter the lenght"))
 print("\n")
h=float(input("Enter the height"))
 print("\n")
b=float(input("Enter the breadth"))
 print("\n")

k=float((l**2+b**2+h**2)**0.5)

v=float((b**2*h**2)/k)
 print("volume of tromboloid",format(v,".3f"))

r=(3*v/(4*math.pi))**(1/3)
 print("radius",format(r,".3f"))
