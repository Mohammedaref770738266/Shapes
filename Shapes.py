import math

class shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(shape):
    def __init__(self,rdius):
        self.rdius = rdius
    def calculate_area(self):
        return math.pi*self.rdius**2

    def calculate_perimeter(self):
        return 2*math.pi*self.rdius


class Triangle(shape):
    def __init__(self,base,height,part1,part2,part3):
        self.base = base
        self.height = height
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3

    def calculate_area(self):
        return 0.5*self.base*self.height

    def calculate_perimeter(self):
        return self.part1+self.part2+self.part3

class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width =width

    def calculate_area(self):
        return self.width*self.length

    def calculate_perimeter(self):
        return 2*(self.length +self.width)

print("welcome in shape calculator\n"
      "choose the shape :")
choice = int(input("1 - circle\n2 - triangle\n3 - rectangle\n4 - exit\n"))
while choice!=4:

    if choice ==1 :
        rdius = int(input("Enter the Rdius\n"))
        circle= Circle(rdius)
        circle_choise = int(input("Enter the number\n1 - area\n2 - perimeter\n3 - Both\n"))
        if circle_choise == 1:
            print(f"The area = {circle.calculate_area()}")
        elif circle_choise == 2:
            print(f"The perimeter = {circle.calculate_perimeter()}")
        elif circle_choise == 3:
            print(f"The area = {circle.calculate_area()}\nThe perimeter ={circle.calculate_perimeter()}")
        else: print("you entered wrong number")


    elif choice ==2:
        base = int(input("Enter the base\n"))
        height = int(input("Enter the height\n"))
        part1 = int(input("Enter the part1\n"))
        part2 = int(input("Enter the part2\n"))
        part3 = int(input("Enter the part3\n"))
        triangle = Triangle(base,height,part1,part2,part3)
        triangle_choise = int(input("Enter the number\n1 - area\n2 - perimeter\n3 - Both\n"))
        if triangle_choise == 1:
            print(f"The area = {triangle.calculate_area()}")
        elif triangle_choise == 2:
            print(f"The perimeter = {triangle.calculate_perimeter()}")
        elif triangle_choise== 3:
            print(f"The area = {triangle.calculate_area()}\nThe perimeter ={triangle.calculate_perimeter()}")
        else: print("you entered wrong number")


    elif choice ==3:
        length = int(input("Enter the length\n"))
        width = int(input("Enter the width\n"))
        rectangle = Rectangle(length,width)
        rectangle_choise = int(input("Enter the number\n1 - area\n2 - perimeter\n3 - Both\n"))
        if rectangle_choise == 1:
            print(f"The area = {rectangle.calculate_area()}")
        elif rectangle_choise == 2:
            print(f"The perimeter = {rectangle.calculate_perimeter()}")
        elif rectangle_choise== 3:
            print(f"The area = {rectangle.calculate_area()}\nThe perimeter ={rectangle.calculate_perimeter()}")
        else: print("you entered wrong number")


    elif choice ==4:
        exit()
    else:
        print("you entered wrong number")

    choice = int(input("1 - circle\n2 - triangle\n3 - rectangle\n4 - exit\n"))

