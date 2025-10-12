"""
Statement : Triangle Classifier Input 3 sides. Check if it's equilateral, isosceles, scalene, or not a triangle.

"""

angles = []
for i in range(1 , 4):
    while True:
        try:
            angle = float(input(f"Enter angle {i}: "))
            if angle > 0:
                angles.append(angle)
                break
            else:
                print("Angle must be positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

a , b , c = angles

if abs( a + b + c - 180) < 0.001:
    if a == b and b == c:
        print("It's an Equilateral triangle")
    elif a == b or a == c or b == c :
        print("It's a Scalene triangle")
else:
    print("The sum of the angles is not 180 degrees . These angles cannot form a triangle.")                  