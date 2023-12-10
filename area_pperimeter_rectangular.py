def calcAreaPeri(length,breadth):
    area=length *breadth
    perimeter=2*(length+breadth)
    return (area,perimeter)
l=float(input("enter length of the rectange:"))
b=float(input("enter breadth of rectangle:"))
#function calling
area,perimeter=calcAreaPeri(l,b)
print("area is",area,"\nperimeter is",perimeter)
