thingdict = {}
class thing:

	def __init__(self,name,taste="",sound="",smell="",feel="",txt=""):
		self.name = name
		self.taste = taste
		self.sound = sound
		self.smell = smell
		self.feel = feel
		self.txt = txt
		
	def speak(self,txt):
		p = "The " + self.name, " says, " + txt

def create(name): #makes a thing
	name = thing(name)
def add(atr,val): #adds an attribute or property to a thing
	if atr == 'taste':
		self.taste = val
	elif atr == 'sound':
		self.sound = val
	elif atr == 'smell':
		self.smell = val
	elif atr == 'feel':
		self.feel = val