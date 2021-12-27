from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import numpy
from random import *
from time import sleep

RF=60
RNOT=0
R1=120
R2=240

x1=0
x2=0




def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)

def drawFlower():
	glPointSize(10.0)
	glColor3f(1,0.6,0.9)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	i=0
	while i<=360:
		glVertex2f(RF*cos(radians(i)),RF*sin(radians(i)))
		i=i+1
	glEnd()

def drawStraw():
	glColor3f(0.8,0.8,0.2)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(0,-400)
	glEnd()

def drawPetal1():


	glColor3f(0.8,0.8,0.2)
	glBegin(GL_LINES)
	glVertex2f(x1,0)
	glVertex2f(0,-400)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(-x1,0)
	glVertex2f(0,-400)
	glEnd()

	glColor3f(1,0.5,0.45)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x1,0)
	i=0
	while i<=360:
		glVertex2f(x1+RF*cos(radians(i)),RF*sin(radians(i)))
		i=i+1
	glEnd()




	glColor3f(0.6,0.89,1)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(-x1,0)
	i=0
	while i<=360:
		glVertex2f(-x1+RF*cos(radians(i)),RF*sin(radians(i)))
		i=i+1
	glEnd()


def drawPetal2():
	glColor3f(0.8,0.8,0.2)
	glBegin(GL_LINES)
	glVertex2f(x2,0)
	glVertex2f(0,-400)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(-x2,0)
	glVertex2f(0,-400)
	glEnd()
	glColor3f(0.6,0.4,0.45)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x2,0)
	i=0
	while i<=360:
		glVertex2f(x2+RF*cos(radians(i)),RF*sin(radians(i)))
		i=i+1
	glEnd()

	glColor3f(0.12,0.32,0.75)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(-x2,0)
	i=0
	while i<=360:
		glVertex2f(-x2+RF*cos(radians(i)),RF*sin(radians(i)))
		i=i+1
	glEnd()
	



def flower():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,1,0)
	drawStraw()
	if x2>=120:
		drawPetal2()
	drawPetal1()
	
	drawFlower()
	
	glutSwapBuffers()


def update(x):
	global x1,x2
	a=0
	if x1<R1:
		x1=x1+1
	elif x1>=R1:
		a=0

	if x2<R2:
		x2=x2+1
	elif x2>=R2:
		return

	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))

def main():

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Moving Fan")
	
	glutDisplayFunc(flower)
	glutTimerFunc(0,update,0)
	glutIdleFunc(flower)
	init()
	glutMainLoop()
main()
