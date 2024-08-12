# Exercise 5-2

# Output Intro
print("-------- Velocity program --------")

# Input
s = float(input("Enter s : "))
t = float(input("Enter t : "))

# Process/Output
v = float(s/t)
if s >= 1 and t >= 1:
    print("v =", v, "(m/s or km/h)")
else:
    print("Value Error!")
