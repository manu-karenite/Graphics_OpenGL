from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import random
import numpy

x=0
y=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)


def createMirror():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0,1,1)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(0,500)
	glVertex2f(0,-500)
	glEnd()


def takeInput():
	global x,y
	x=float(input("Please enter the x coordinate : "))
	y=float(input("Pleas enter the y coordinate : "))
	return

def printGivenPoint():
	glColor3f(0,1,0.5)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()

def printReflectedPoint():
	glColor3f(1,0,0)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(-x,y)
	glEnd()

def plot():
	createMirror()
	printGivenPoint()
	printReflectedPoint()
	glFlush()



def main():
	takeInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("MIrror")
	glutDisplayFunc(plot)
	glutIdleFunc(plot)
	init()
	glutMainLoop()


main()