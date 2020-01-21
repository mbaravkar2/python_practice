triangle = int(input("Enter the angle :"))
if triangle == 90 or triangle <= 90:
    print("First Quadrant")
elif triangle== 180 or (triangle >= 90 and triangle <=180):
    print("Second Quadrant")
elif triangle == 270 or (triangle >= 180 and triangle <= 270):
    print("Third quadrant")
elif triangle == 360 or (triangle >= 270 and triangle <=360):
    print("Fourth quadrant")
