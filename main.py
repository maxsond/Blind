import display
from display import msg #Contains everything to do with displaying output to the player
import time
from parse import read
import curses
import creator
from winsize import x, y
x = x()
y = y()

def introduce():
	intro = msg(y/2,x/2,0.5,"BLIND",'center')
	intro.tw(False)
	intro = msg(y/2+2,x/2,0.1,"A text-based sandbox game",'center')
	intro.tw(False)
	intro = msg(y/2+3,x/2,0.1,"By Daniel Maxson",'center')
	intro.tw(True)
	display.clear()
	itxt = "It is pitch black. You are likely to be blind."
	intro = msg(y/2,x/2,0.1,itxt,'center')
	intro.tw(True)

def prompt():
	p = "What do you do?"
	h = len(p)/2
	q = msg(y/2,x/2-h,0.1,p,'right')
	i = display.inp(q)
	read(i)
introduce()
while True:
	display.clear()
	prompt()
display.end()