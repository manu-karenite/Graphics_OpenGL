from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import random
from pygame import mixer


mixer.init()
mixer.music.load("/home/manavesh/Downloads/Noddy - Theme Song.mp3")
mixer.music.set_volume(0.75)
x1=0
y1=0
vx=vy=1
speed=1
TO_RIGHT=0
TO_TOP=1
HORN=False



def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-200,200,-200,200)

def start():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(10.0)
	glBegin(GL_POLYGON)
	glVertex2f(x1+20,y1+20)
	glVertex2f(x1-20,y1+20)
	glVertex2f(x1-20,y1-20)
	glVertex2f(x1+20,y1-20)
	glEnd()
	glutSwapBuffers()

def update(value):
	global x1,y1
	global TO_RIGHT,TO_TOP
	global vx,vy
	if TO_RIGHT==0:
		#Means that there is no movement in x direction
		if TO_TOP==1:
			#Means that we have movement in +y direction
			if y1<180:
				y1=y1+0.5
			else:
				TO_TOP=-1

		elif TO_TOP==-1:
			if y1>-180:
				y1=y1-0.5
			else:
				TO_TOP=1

	elif TO_TOP==0:
		#Means that there is no movement in x direction
		if TO_RIGHT==1:
			#Means that we have movement in +y direction
			if x1<180:
				x1=x1+0.5
			else:
				TO_RIGHT=-1

		elif TO_RIGHT==-1:
			if x1>-180:
				x1=x1-0.5
			else:
				TO_RIGHT=1
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)


def keyboardControls(key,x,y):
	global TO_RIGHT,HORN,TO_TOP,speed
	if key==b'a':
		TO_TOP=0
		TO_RIGHT=-1
	elif key==b'd':
		TO_TOP=0
		TO_RIGHT=1
		
	elif key==b'h' and HORN==False:
		HORN=True
		mixer.music.play()
	elif key==b'h' and HORN==True:
		HORN=False
		mixer.music.stop()
	elif key==b'w':
		TO_RIGHT=0
		TO_TOP=1
	elif key==b's':
		TO_RIGHT=0
		TO_TOP=-1
	elif key==b'=':
		speed=speed+0.2
	elif key==b'-':
		speed=speed-0.2

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA )

	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,00)
	glutCreateWindow("Square Animation")

	glutDisplayFunc(start)
	glutTimerFunc(0,update,0)
	glutKeyboardFunc(keyboardControls)
	glutIdleFunc(start)
	init()
	glutMainLoop()

main()
