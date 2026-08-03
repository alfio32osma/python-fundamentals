def area (length, width):
    print(str(length * width) + " Square feet")
    return length * width

def main():
    house = area(10, 25)
    yard = area(5, 10)
    total = house + yard
    print(str(total) + " Total Square Feet")

main()