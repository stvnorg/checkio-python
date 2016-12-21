import math

def checkio(data):
	len_list = sorted(data)
	a = len_list[0]
	b = len_list[1]
	c = len_list[2]
	angle = []
	angle_a = 0
	angle_b = 0
	angle_c = 0
	if (a+b) <= c:
		return [0,0,0]
	else:
		angle_a = int(round(math.degrees(math.acos((a**2-(b**2+c**2))/1.0/-(2*b*c)))))
		angle_b = int(round(math.degrees(math.acos((b**2-(a**2+c**2))/1.0/-(2*a*c)))))
		angle_c = 180 - angle_a - angle_b
		
	return sorted([angle_a,angle_b,angle_c])

print (checkio([2,2,5]))
print (checkio([3,4,5]))
print (checkio([4,4,4]))

