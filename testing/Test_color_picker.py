import random, time #Time is just for simulation purposes

def Color_Randomizer():
	WHITE     =  (255,255,255)
	BLACK     =  (  0,  0,  0)
	RED       =  (255,  0,  0)
	GREEN     =  (  0, 255, 0)
	BLUE      =  (  0,   0, 0) 
	DARKGREEN =  (  0, 150, 0)
	DARKGRAY  =  ( 40, 40, 40)


	active_colors = [
		"WHITE",
		"BLACK",
		"RED",
		"GREEN",
		"BLUE",
		"DARKGREEN",
		"DARKGRAY",
	 ] # 7
	 
	 
	console = """
	 \n
	 Font_Color: {0}
	 Background Color: {1}
	 Position: {2}
	 Font Size: {3}
	 Debug Mode: {4}
	 
	 """
	 
	def command_sim():
		
		# Turn these calls to random.randint into lambdas that are
		# called only when the button is pressed in the Arduino...
		# Also these calls need to be completely optomized for the 
		# pi.
		# Easier said than done.  
		
		fontColor = active_colors[random.randint(0,6)]
		bckColor = active_colors[random.randint(0,6)]
		position = str((random.randint(1,800), random.randint(1,600)))
		font_size = random.randint(1,50)
		Debug_mode = "False"
		
		return console.format(fontColor, bckColor, position, font_size, Debug_mode)
		
	while True:
		time.sleep(1)
		print command_sim()
