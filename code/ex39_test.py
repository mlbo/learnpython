stuff = {'name': 'Li', 'age': 25, 'height': 6*12+2, 'b': 'b'}
print stuff['name']
print stuff['age']
print stuff['height']
print stuff
stuff['city'] = "TongLing"
stuff[1] = "Apple"
print stuff[1]
print stuff
del stuff[1]
print stuff
# print stuff.pop('name')
# print stuff
# print stuff.items()
# print ('city', "TongLing") in stuff.items()
# print stuff.values()
# print stuff.viewitems()
# print stuff.viewvalues()
for key, value in stuff.items():
	print "%s is  %s" % (key, value)
