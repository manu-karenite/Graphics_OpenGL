from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy
import sys

#global here
RADIUS_SUN=60
RX1=300
RY1=150
RP1=30

RX2=440
RY2=220
RP2=40


THETA=0
def init():
	gluOrtho2D(-500,500,-500,500)
	glClearColor(0,0,0,1)

def plotAxes():
	#print the coordinate exes first
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(0,500)
	glVertex2f(0,-500)
	glEnd()


def plotGrids():
	#at 50 intervals
	x=-500
	y=0
	glLineWidth(1.5)
	while y<=500:
		glColor3f(0.6,0.8,0.45)
		glBegin(GL_LINES)
		glVertex2f(-500,y)
		glVertex2f(500,y)
		glEnd()

		glBegin(GL_LINES)
		glVertex2f(-500,-y)
		glVertex2f(500,-y)
		glEnd()

		glColor3f(0.1,0.1,0.45)
		glBegin(GL_LINES)
		glVertex2f(y,500)
		glVertex2f(y,-500)
		glEnd()

		glBegin(GL_LINES)
		glVertex2f(-y,500)
		glVertex2f(-y,-500)
		glEnd()
		y=y+100

def drawSun():
	glColor3f(cos(THETA),1,0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	i=0
	while i<=360:
		glVertex2f(RADIUS_SUN*cos(radians(i)),RADIUS_SUN*sin(radians(i)))
		i=i+2
	glEnd()

def drawOrbit1():
	i=0
	glColor3f(0.4,0.4,0.4)
	glPointSize(6.0)
	glBegin(GL_POINTS)
	while i<=360:
		glVertex2f(RX1*cos(radians(i)),RY1*sin(radians(i)))
		i=i+1
	glEnd()
def drawPlanet1():
	#calculate the cxentres first
	glColor3f(0.5,0.7,0.4)
	x=RX1*cos(radians(THETA))
	y=RY1*sin(radians(THETA))
	i=0
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	while i<=360:
		glVertex2f(x+RP1*cos(radians(i)),y+RP1*sin(radians(i)))
		i=i+1
	glEnd()

def drawOrbit2():
	i=0
	glColor3f(0.4,0.4,0.4)
	glPointSize(6.0)
	glBegin(GL_POINTS)
	while i<=360:
		glVertex2f(RX2*cos(radians(i)),RY2*sin(radians(i)))
		i=i+1
	glEnd()
def drawPlanet2():
	#calculate the cxentres first
	glColor3f(0.5,0.7,0.4)
	x=RX2*cos(radians(THETA))
	y=RY2*sin(radians(THETA))
	i=0
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	while i<=360:
		glVertex2f(x+RP2*cos(radians(i)),y+RP2*sin(radians(i)))
		i=i+1
	glEnd()
		


def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	#plotGrids()
	plotAxes()
	drawSun()
	drawOrbit1()
	drawPlanet1()

	drawOrbit2()
	drawPlanet2()
	glutSwapBuffers()

def update(x):
	
	global THETA
	THETA=(THETA+1)%360
	glutTimerFunc(int(1000/60),update,int(0))
	glutPostRedisplay()
	

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(800,800)
	glutCreateWindow("Solar System")
	glutDisplayFunc(plot)
	glutTimerFunc(0,update,0)
	glutIdleFunc(plot)
	init()
	glutMainLoop()

main()
