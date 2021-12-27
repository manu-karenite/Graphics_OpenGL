from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import numpy
from random import *
from time import sleep

FLAP=150
ANGLE1=60
ANGLE2=120
OPEN=True
xc=0
yc=0


def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)


def drawBird():
	glColor3f(1,1,0)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(xc,yc)
	glVertex2f(xc+FLAP*cos(radians(ANGLE1)),yc+FLAP*sin(radians(ANGLE1)))
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(xc,yc)
	glVertex2f(xc+FLAP*cos(radians(ANGLE2)),yc+FLAP*sin(radians(ANGLE2)))
	glEnd()
def drawFan():
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(10.0)
	glColor3f(0,0,1)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()

	drawBird()
	glFlush()

def redraw(x):
	sleep(0.8)
	global ANGLE1,ANGLE2,FLAP,xc,yc,OPEN
	if OPEN==True:
		ANGLE1=85
		ANGLE2=95
		OPEN=False
	elif OPEN==False:
		ANGLE1=60
		ANGLE2=120
		OPEN=True

	xc=randint(-400,400)
	yc=randint(-400,400)


	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,int(0))

def main():

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Moving Fan")
	
	glutDisplayFunc(drawFan)
	glutTimerFunc(0,redraw,0)
	glutIdleFunc(drawFan)
	init()
	glutMainLoop()
main()