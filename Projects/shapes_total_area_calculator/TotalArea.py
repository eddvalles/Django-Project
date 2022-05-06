from shapes import Triangle, Circle, Rectangle

def main():
    shapes_container = [] # Container that will hold all shape objects

    valid_shapes = ["Triangle", "Circle", "Rectangle"]
    valid_shape = False

    while True:
        shape = input("Please enter a shape to calculate ('Triangle', 'Circle', 'Rectangle'): 'done' to end")

        if shape == 'done': break

        if shape in valid_shapes: # Verifies that a valid shape was input
            valid_shape = True

        if valid_shape: # If the user entered a valid shape
            if shape == 'Triangle': # If the shape is a Triangle
                while True:
                    try:
                        a = float(input("Please enter side one: "))
                        b = float(input("Please enter side two: "))
                        c = float(input("Please enter side three: "))

                        if ((a + b > c) and (b + c > a) and (a + c > a)): # Validate the triangle sides
                            myTriangle = Triangle(a, b, c)

                            shapes_container.append(myTriangle)

                            break
                        else:
                            print("The three sides do not form a triangle!\nPlease try again.")
                    except ValueError as e:
                        print(f"Please enter valid numbers ! {e}")
            if shape == 'Rectangle': # If the shape is a Rectangle
                while True:
                    try:
                        length = float(input("Please enter the length: "))
                        width = float(input("Please enter the width: "))

                        myRectangle = Rectangle(length, width)

                        shapes_container.append(myRectangle)

                        break
                    except ValueError as e:
                        print(f'Please enter valid numbers ! {e}')
            if shape == 'Circle': # If the shape is a Circle
                while True:
                    try:
                        radius = float(input("Please enter the radius: "))

                        myCircle = Circle(radius)

                        shapes_container.append(myCircle)

                        break
                    except ValueError as e:
                        print(f'Please enter a valid number ! {e}')
        else:
            print("I cannot calculate that !")

    print()
    # Output the perimeter and area of each shape provided
    for shape in shapes_container:
        shape.calculate_area() # Calculates the area for each shape object in the shape list
        shape.calculate_perimeter() # Calculates the perimeter for each shape object in the shape list

        shape_name = 'Triangle' if isinstance(shape, Triangle) else \
                'Rectangle' if isinstance(shape, Rectangle) else \
                'Circle' if isinstance(shape, Circle) else None
        print(f'Perimeter of {shape_name} is: {shape.get_perimeter():.2f}')
        print(f'Area of {shape_name} is: {shape.get_area():.2f}\n')


if __name__ == '__main__':
    main()