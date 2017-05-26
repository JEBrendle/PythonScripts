import math

print("Input alpha:"),
alpha = input()

print("Input beta:")
beta = input()

print("Input gamma:")
gamma = input()

phi = float(alpha)*(math.pi/180)
theta = float(beta)*(math.pi/180)
sigma = float(gamma)*(math.pi/180)

e0 = math.cos(theta/2)*math.cos((phi+sigma)/2)
e1 = math.sin(theta/2)*math.cos((phi-sigma)/2)
e2 = math.sin(theta/2)*math.sin((phi-sigma)/2)
e3 = math.cos(theta/2)*math.sin((phi+sigma)/2)

print("The quaternion coordinates are: [", e0, ", ", e1, ", ", e2, ", ", e3, "]")
