#-*- coding: utf-8 -*-
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y ="Those who know %s and those who %s" % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = 'False'
joke_evaluation = "Isn't that joke so funny! %r"
joke_evaluation1 = "Isn't that joke so funny! %s"

print joke_evaluation % hilarious
print joke_evaluation1 % hilarious
e = "a string with a right side"
w = "This is the left side of ..."

print w + e
print 'let\'s go' #转义字符
print"""
Hello World
Hello World
Hello World
Hello World
"""
string = r'c:\now'
string1= 'c:\now'
print string
print string1