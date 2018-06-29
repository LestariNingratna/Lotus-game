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
		print """\033[1;31m
                     Lotus in The Underworld
		     developed by Lestari Ningratna Sari
	             2018 
                     \x1b[0m
                      """
		print """
                                                        --------
		     You just woke up in a big and luxurious bedroom. You can't remember anything.
		     You try to recall, and it's getting weird because you don't even remember your name.
		     From large windows across the room in front of you, the bright morning light striking into the room.
	             You see a wooden table near the windows."
	             There's a letter on the table. Type \"read\" to read the letter.
                     """
		
		action = raw_input("> ").lower()
		if action == "read":
			print """
                                  +==================================================================================================================+"
			         "|                                          WELCOME TO THE UNDERWORLD                                               |"
		        	 "|                                                                                                                  |"
		        	 "+==================================================================================================================+"
		        	 "| This place is a dangerous place that can mislead anyone in it. If you are stranded here, you need to escape.     |"
		        	 "| To be able to escape from the underworld, you need to finish your mission.                                       |"
		        	 "| And to be able to do it, you need to know what your mission is.                                                  |"
			         "| Unfortunately, you will never find the answer here.                                                              |"
		        	 "| You need to regain your memory to find out what your mission is.                                                 |"
		        	 "| But don't worry, you will get a beautiful lotus in your hand to guide you and find the answer.                   |"
		        	 "|                                                                                                                  |"
		        	 "|                                                   *****                                                          |"
		        	 "+==================================================================================================================+"
		        	 "                                                    ....."
		        	 "                                                     ..."
			 
                                                                                         .
                               """

			return 'lotus_mansion'
		else:
			print "DOES NOT COMPUTE!"
			return 'prolouge'
			
class LotusMansion(Scene):
	def enter(self,MainCharacter):
		print """
                                A beautiful lotus magically appears in your hand out of thin air. A blooming red lotus.
		                Very unusual because the color is bright red like the color of blood.
		                You look at the flower and wondering how it suddenly appears, a sudden loud voice startled you.
		                Someone's knocking the front door. You step out of the bedroom, walking through the hallway to reach the front door.
		                The house is so big and spacious it's more similar to mansion than a normal house.
		                You open the door and you see a little boy with his white pyrenean mountain dog.
		                \"Sir, my dog has been following the smell of lotus flower in your house.\"
		                \"My dog told me that you can help me find my home.\""
		                \"I've been walking for 3 days with my dog, and I couldn't find my way to home.\"
		                \"Would you mind to help me? Please...\", said the little boy"
		                You see the lotus in your hand is shining so bright, and suddenly one of its petals fall off.
		                This little boy could be a clue for you to escape the underworld. Do you want to help him? (y/n)
                    """
		
                action = raw_input("> ").lower()
                
		if action == "y":
			print """
                                ---------------------------------------------------------
			        You decided to help him. Try to ask something to him!"
			        1. \"What\'s your name?\"
			        2. \"Where do you live?\"
			        3. \"Your dog can talk?\"
			        4. \"Do you know anything about my weird flower?\"
			        5. \"alright. Let's find your home\"
                         """
			return 'dialouge'
		
		elif action == "n":
			print """
                                Like a world class boxer you dodge, weave, slip and slide right"
			        as the Gothon's blaster cranks a laser past your head."
			        In the middle of your artful dodge your foot slips and you"
			        bang your head on the metal wall and pass out."
			        You wake up shortly after only to die as the Gothon stomps on"
			        your head and eats you."
			"""
		else:
			print "DOES NOT COMPUTE!"
			return 'lotus_mansion'

class Dialouge(Scene):
	def enter(self,MainCharacter):
		action = raw_input("> ").lower() 

		if action == "1":
			print """
                               You asked: 1. \"What's your name?\"
			       \"my name is Liam... Liam Dayton. and my dog's name is Snowy\", said the kid.
			       \"May I know your name, sir?\"
			       You don't know what to say, because you don't even remember yours
			       \"Uh.... I don't remember my name\"
			       \"That's weird. Okay.... can I call you Mr. Lotus?\", asked the kid
			       \"It sounds funny. Well, it's okay... you can call me Mr. Lotus. Nice to meet you Liam!\"
                         """
			return 'dialouge'
		
		elif action == "2":
			print """
                               You asked: 2. \"Where do you live?\"
			       \"I don't remember...\""
			       \"That's why I asked for your help\"
			       \"Snowy knows where is it. But he's blind and he can't smell very well\"
			       \"The only thing he can smell is your flower\"
                         """
			return 'dialouge'
		
		elif action == "3":
			print """
                              You asked: 3. \"Your dog can talk?\"
			      \"You can't hear it? Look he just talked to me!\", said Liam
			      \"No, I can't hear it.\" you said
			      \"You can't hear it? but he just talked\"
			      \"woof!\", the dog barked and wagging his tail
			      You think this kid's imagination is too wild.
			      But after all of the weird things that just happened to you,
			      it might be real. This kid might be able to talk to his dog
			      \"what did Snowy say to you?\""
			      \"He said you smell like a good person and he trust you\"
                                """
			return 'dialouge'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'dialouge'
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
