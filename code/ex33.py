
numbers = []

def while_teat(last):
	i = 0

	while i< last:
		print "At the top i is %d" % i
		# str1 = "please input " + str(i) + "i: "
		# m= raw_input(str1)
		# numbers.append(m)
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

while_teat(6)

print "The numbers: "

for num in numbers:
	print num