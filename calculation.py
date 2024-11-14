import math as m
from decimal import Decimal

print("here is some of the calculation you want to be done for you")
print("1. Area")
print("2. Perimeter")
print("3. quandratic equation")
num = int(input("enter the tpe of calclation you want it to be done for you: "))

def Area():
      print("<------------ here are the area we can calculate for you ---------->")
      print("1. Area of the circle")
      print("2. Area of the rectangle")
      print("3. Area of the triangle")
      print("4. Area of the sphere")
      print("5. Area of the square")
      type1= int(input(" enter the area you want to be calculated:"))
      def area_of_the_circle():
            radius=  int(input("Enter the radius of the circle: "))
            result = m.pi * radius**2
            result =  round(result, 2)
            print(result)

      def  area_of_rectangle():
            print("enter the dimessions of the rectangle")
            height = int(input("enter the height of the rectangle"))
            width = int(input("enter the width of the rectangle"))
            arear = height * width
            arear = round(arear, 2)
            print("the area of a rectangle is ", arear)

      def area_of_the_triangle():
            print("<--------  Which  type of triangle are we calculating  ---------->")
            print("1. Right angled triangle")
            print("2. Equivalent/isocless triangle")
            type2 = int(input("enter which type of triangle are we calculating: "))
            height = int(input("enter the height of the triangle: "))
            base = int(input("enter the base: "))
            if  type2 == 1:
                  answer = (height * base) / 2
                  answer = round(answer, 2)
                  print("the area of the triangle is ", answer)
            elif type2 == 2:
                  base = base /2
                  answer = height * base
                  answer = round(answer, 2)
                  print("the area of the triangle is ", answer)

      def area_of_sphere():
            radiuss = int(input("enter the area of the sphere:  "))
            areas = 4 * m.pi *radiuss**2
            areas = round(areas, 2)
            print(areas)

      def area_of_square():
            widths = int(input("enter the width of the square: "))
            areas = widths**2
            areas = round(areas, 2)
            print(areas)

      def run_area():
            while True:
                  try:
                        match type1:
                              case 1:
                                    area_of_the_circle()
                                    break
                              case 2:
                                    area_of_rectangle()
                                    break
                              case 3:
                                    area_of_the_triangle()
                                    break
                              case 4:
                                    area_of_sphere()
                                    break
                              case 5:
                                    area_of_square()
                                    break
                              case _:
                                    print("invalid number please try again")

                        break
                  except ValueError:
                         print("Invalid input. Please enter a number.")
      run_area()
def  Perimeter():
      print("<------------here is the calculation available for perimeter------------->")
      print("1. Perimeter of the circle")
      print("2. Perimeter of the rectangle")
      print("3. Perimeter of the triangle")
      print("4. Perimeter of the sphere")
      print("5. Perimeter of the square")
      perimeter = int(input("Enter the perimeter you want to be calculated: "))

      def circle():
           diameter =  int(input("enter the diameter of the circle or 2r: "))
           perimeter_cir = m.pi * diameter
           perimeter_cir = round(perimeter_cir , 2)
           print("the perimeter of the circle is : ", perimeter_cir)
      
      def triangle():
            dim1 = int(input("enter the first length of the triangle: "))
            dim2 = int(input("enter the second length of the triangle: "))
            dim3 = int(input("enter the third length of the triangle: "))
            total = dim1 + dim2 + dim3
            total = round(total , 2)
            print("the perimeter of the triangle is: ", total)

      def sphere():
            radiuss = int(input("enter the radius of the sphere: "))
            peri = 2 *m.pi * radiuss
            peri = round(peri, 2)
            print("the perimeter of a sphere is ", peri)

      def square():
            length = int(input("enter the length of the square: "))
            squa = length * 4
            print("the perimeter of a square is" , squa)
      def run_perimeter():
            match perimeter:
                  case 1:
                        circle()
                  case 2:
                        triangle()
                  case 3:
                        sphere()
                  case 4:
                        square()
                  case _:
                        print("you have enter the wrong input please try again")
                        return
      
      run_perimeter()
def quadratic_equation():
      a = int(input("enter the coefficient of a: "))
      b = int(input("enter the coefficient of b: "))
      c = int(input("enter the coefficient of c: "))
      
def runcase():
      match num:
            case 1:
                  Area()
            case 2:
                  Perimeter()
            case 3:
                  quadratic_equation()
            

runcase()