import time
import curses
from winsize import x, y
x = x()
y = y()
q = "What do you do?"
win = curses.initscr()
win.border(0)
win.refresh()
class msg:
	
	def __init__(self,y=0,x=0,speed=0.1,txt="Test String",align='right'):
		self.txt = txt
		self.x = x + 1
		self.y = y + 1
		self.speed = speed
		self.align = align
		
	def al(self, align):	#Represents how the text should be horizontally aligned relative to (x,y)
		if align == 'right':
			return self.x
		elif align == 'center':
			return self.x - len(self.txt)/2
		elif align == 'left':
			return self.x - len(self.txt)

	def tw(self,wait):
		"""Taps out a message like a typewriter.

		msg -> Message to be tapped out
		w -> Window to work in
		x,y -> Where the cursor should start
		"""
		#try:
		win.move(self.y,self.al(self.align))
		for c in self.txt:
			win.addch(c)
			win.refresh()
			time.sleep(self.speed)
#		except:
#			self.win.clear
#			curses.endwin()
#			print ""
#			print "Fatal error! Cursor went out of bounds!", self.x, self.y
		if wait:
			win.getch()
		win.border(0)
		win.refresh()
def end():
	win.erase()
	win.refresh()
	curses.endwin()
def clear():
	win.erase()
	win.border(0)
	win.move(1,1)
	win.refresh()
def inp(msg):
	win = curses.initscr()
	try:
		msg.tw(False)
		#print msg.y+1, msg.al('right')
		return win.getstr(msg.y+1,msg.x)
		#print win.is_wintouched()
		#print xyz.is_wintouched()
		win.refresh()
	except:
		exit()
def test():
	time.sleep(0.5)