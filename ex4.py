cars = 100
#the space of one car
space_in_a_car = 4.0
#The number of drivers
drivers = 30
#The number of passengers
passengers = 90
cars_not_driven = cars - drivers
cars_diven = drivers
#The capacity of all car 
carpool_capacity = cars_diven * space_in_a_car
average_passengers_per_car = passengers / cars_diven



print "There are",cars,"cars available"
print "There are only",drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today"
print "We can transport",carpool_capacity,"people today"
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car"