from sys import exit

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):
	
	def __init__(self, scene_map,MainCharacter):
		self.scene_map = scene_map
		self.MainCharacter = MainCharacter
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter(self.MainCharacter)
			current_scene = self.scene_map.next_scene(next_scene_name)
			
class Prolouge(Scene):
	def enter(self,MainCharacter):
		print "Lotus in The Underworld"
		print "developed by Lestari Ningratna Sari"
		print "2018"
		print "--------"
		print "You just woke up in a big and luxurious bedroom. You can't remember anything."
		print "You try to recall, and it's getting weird because you don't even remember your name."
		print "From large windows across the room in front of you, the bright morning light striking into the room."
		print "You see a wooden table near windows."
		print "There's a letter on the table. Type \"read\" to read the letter."
		
		action = raw_input("> ")
		if action == "read":
			print "\n+==================================================================================================================+"
			print "|\t \t \t \t \t   WELCOME TO THE UNDERWORLD                                               |"
			print "|                                                                                                                  |"
			print "+==================================================================================================================+"
			print "| This place is a dangerous place that can mislead anyone in it. If you are stranded here, you need to escape.     |"
			print "| To be able to escape from the underworld, you need to finish your mission.                                       |"
			print "| To be able to finish your mission, you need to know what your mission is.                                        |"
			print "| Unfortunately, we don't have the answer here. You need to regain your memory to find out what your mission is.   |"
			print "| But don't worry, you will get a beautiful lotus in your hand to guide you to find the answer.                    |"
			print "|                                                                                                                  |"
			print "|\t \t \t \t \t \t    *****                                                          |"
			print "+==================================================================================================================+"
			print "                                                    ....."
			print "                                                     ..."
			print "                                                      ."
			return 'lotus_mansion'
		else:
			print "DOES NOT COMPUTE!"
			return 'prolouge'
			
class LotusMansion(Scene):
	def enter(self,MainCharacter):
		print "A beautiful lotus magically appears in your hand out of thin air. A blooming red lotus."
		print "Very unusual because the color is bright red like the color of blood."
		print "You're observing the flower and wondering how it suddenly appears, a sudden loud voice startled you."
		print "Someone's knocking the front door. You step out of the bedroom, walking through the hallway to reach the front door."
		print "The house is so big and spacious it's more similar to mansion than a normal house."
		print "You open the door and you see a little boy with his white pyrenean mountain dog."
		print "\"Sir, my dog is smelling the smell of lotus flower in your house. My dog told me that you can help me find my home."
		print "I have been walking for 3 days with my dog, and I can not find my way to my home. Would you mind to help me? Please...\", said the little boy"
		print "You see the lotus in your hand is shining so bright, and suddenly one of its petals fall off."
		print "This little boy could be a clue for you to escape the underworld. Do you want to help him? (y/n)"
		
		action = raw_input("> ")
		if action == "y":
			print "You decided to help him. Try to ask something to him!"
			return 'dialouge'
		
		elif action == "n":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			
		else:
			print "DOES NOT COMPUTE!"
			return 'lotus_mansion'

class Dialouge(Scene):
	def enter(self,MainCharacter):
		print "1. \"What\'s your name?\""
		print ""
		print ""
class Map(object):

	scenes = {'prolouge' : Prolouge(),
		'lotus_mansion' : LotusMansion(),
		'dialouge' : Dialouge()}
	
	def __init__(self,start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
				
class MainCharacter():
	''' class for hero '''
	
	hp = 1000
	power = 200
	rate = 5

a_map = Map('prolouge')
a_game = Engine(a_map,MainCharacter)
a_game.play()