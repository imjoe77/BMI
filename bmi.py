import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = sys.argv[1]
    height = sys.argv[2]
else:
    script_name = sys.argv[0]
    weight = 60
    height = 170
print("Invalid input using default values")
weight = float(weight)
height = float(height) / 100
bmi = weight / (height*height)
print("Weight", weight, "kg")
print("Height", height, "m")
print("BMI", bmi)
