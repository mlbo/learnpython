def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtraCt(a, b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a, b):
	print "multiply %d * %d" % (a,b)
	return a * b

def divide(a, b):
	print "divide %d / %d" % (a,b)
	return a / b


print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtraCt(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, height: %d, weight: %d,iq: %d"%(age,height,weight,iq)

# #A puzzle for the extra creditd, type it in anyway.
# print "Here is puzzle."

# i1 = divide(iq, 2)
# i2 = multiply(weight, i1)
# i3 = subtraCt(height,i2)
# what = add(age,i3)
# # what = add(age,subtraCt(height, multiply(weight, divide(iq, 2))))
# print "That becomes: ", what,"Can you do it hand?"
num = subtraCt(add(24,divide(34, 100)), 1023 )

print num
