#-*- coding: utf-8 -*-
from sys import exit
def older_room():
	print "When you see an old man fall,"
	print "but you don’t have first aid knowledge."
	print "What would you do?"
	print "(1)、Dial 120 and ask people who know first aid"
	print "(2)、Lifting the elderly directly"
	print "(3)、Pretend not to see it, go straight away"
	print "Please choose 1 or 2 or 3"
	next = raw_input("> ")
	if next == "1":
		gold_room()
	elif next == "2":
		bear_room()
	elif next == "3":
		cthulhu_room()
	else:
		print "Please choose right number"
		older_room()

def child_room():
	print "If you find a child falling into water,"
	print "but you can't swim."
	print "What would you do?"
	print "(1)、Dial 120 and ask people who can swim"
	print "(2)、Jump directly into the water to save child"
	print "(3)、Pretend not to see it, go straight away"
	print "Please choose 1 or 2 or 3"
	next = raw_input("> ")
	if next == "1":
		gold_room()
	elif next == "2":
		bear_room()
	elif next == "3":
		cthulhu_room()
	else:
		print "Please choose right number"
		child_room()


def gold_room():
	print "This room  is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Man, you're not greedy and loving, you win!"
		exit(0)
	else:
		dead("You are a caring person, but too greedy!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		older_room()
	elif next == "right":
		child_room()
	else:
		dead("You stumble around the room until you starve")


start()