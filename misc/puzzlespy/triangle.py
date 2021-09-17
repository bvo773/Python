def typeOfTriangle(side1, side2, side3):
    if (side1 == side2 == side3):
        return "Equilateral triangle"
    elif(side1 != side2 != side3):
        return "Scalene triangle"
    else:
        return "Isoceles triangle"
        

        
def main():
    triangle1 = typeOfTriangle(10, 10, 10)
    triangle2 = typeOfTriangle(10, 10, 20)
    triangle3 = typeOfTriangle(10, 20, 30)
    print("{} | {} | {} ".format(triangle1, triangle2, triangle3))

if __name__ == "__main__":
    main()

    
