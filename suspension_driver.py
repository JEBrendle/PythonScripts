# Author: Jacob Brendle
# This Python script outputs the needed driver to run the Chrono Suspension Test Rig
### PYTHON 3.6 ONLY ###

driver = open('driver.dat', 'w') # File name can be changed as desired

end = 24 # Simulation length

# Fill time[] until it reaches the simulation length with a 0.1 step
t = 1
time = []
while t <= end:
	time.append(round(t, 1))
	t+=0.1

LWH = 0.00 # Initial Left Wheel Height
RWH = 0.00 # Initial Right Wheel Height
SA 	= 0.00 # Initial Steering Angle

left_wheel 	= [] # Array that will be filled with left wheel heights
right_wheel = [] # Array that will be filled with right wheel heights
steering 		= [] # Array that will be filled with steering angles

# Begin raising and lowering left wheel
while LWH <= 1:
	left_wheel.append(round(LWH, 2))
	LWH += 0.05

while LWH >= 0:
	left_wheel.append(round(LWH, 2))
	LWH -= 0.05
# End

# Begin lowering and raising left wheel
while LWH >= -1:
	left_wheel.append(round(LWH, 2))
	LWH -= 0.05
	
while LWH <= 0:
	left_wheel.append(round(LWH,2))
	LWH += 0.05
# End

# So that both wheels do not move up and down at the same time,
# zeros to the beginning of the right wheel
while len(right_wheel) <= len(left_wheel):
	right_wheel.append(0.00)

# Fill left_wheel[] so that it is the same length as time[]
while len(left_wheel) <= len(time):
	left_wheel.append(0.00)

# Begin raising and lowering right wheel
while RWH <= 1:
	right_wheel.append(round(RWH, 2))
	RWH += 0.05
	
while RWH >= 0:
	right_wheel.append(round(RWH, 2))
	RWH -= 0.05
# End
	
# Begin lowering and raising right wheel
while RWH >= -1:
	right_wheel.append(round(RWH, 2))
	RWH -= 0.05

while RWH <= 0:
	right_wheel.append(round(RWH, 2))
	RWH += 0.05
#End

# So that there is no steering while the wheels are being raised and lowered,
# push zeros to the beginning of the steering angle
while len(steering) <= len(right_wheel):
	steering.append(0.00)

# Fill right_wheel[] so that it is the same length as time[]
while len(right_wheel) <= len(time):
	right_wheel.append(0.00)
		
# Steer the tires
while SA >= -1:
	steering.append(round(SA, 2))
	SA -= 0.05

while SA <= 1:
	steering.append(round(SA, 2))
	SA += 0.05
	
while SA >= 0:
	SA -= 0.05
# End

# Fill steering[] so that it is the same length as time[]
while len(steering) <= len(time):
	steering.append(0.00)

# Write the values to the data file
initial = [0.00, 0.00, 0.00, 0.00]
y = 0
while y < len(initial):
	driver.write(str(initial[y]))
	driver.write(" ")
	y += 1

driver.write('\n')

x = 0

while x < len(time):
	driver.write(str(time[x]))
	driver.write("\t")
	driver.write(str(left_wheel[x]))
	driver.write("\t")
	driver.write(str(right_wheel[x]))
	driver.write("\t")
	driver.write(str(steering[x]))
	driver.write('\n')
	x += 1
