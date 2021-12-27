from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
from math import *

theta_min=60
theta_max=120
radius=0

def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(0,1000,0,200)
	

def drawMountains():
	i=1
	#while i<=5:
	x=0
	xbar=0
	while i<=5:
		x=xbar
		glColor3f(0.81,0.7,.6)
		glBegin(GL_TRIANGLE_FAN)
		glVertex2f(x,0)
		
		glVertex2f(x+200,200*tan(radians(30)))
		glVertex2f(x+400,0)
		glEnd()

		xbar=x+400
		i=i+1

def drawSun():
	i=30
	while i<=150:
		#get the sun's vertex
		x=400
		y=0
		#xnew=x*cos(radians(i))-y*sin(radians(i))
		#ynew=x*sin(radians(i))+y*cos(radians(i))
		xnew=x+radius*cos(radians(i))
		ynew=y+radius*sin(radians(i))
		glColor3f(1,1,0)
		glPointSize(100.0)
		glBegin(GL_POINTS)
		glVertex2f(xnew,ynew)
		glVertex2f(-xnew,ynew)
		glVertex2f(400,0)
		glEnd()
		i=i+1

def update(value):
	#update here
	global radius
	if radius<60:
		radius=radius+1
	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))


def start():
	glClear(GL_COLOR_BUFFER_BIT)
	drawSun()
	drawMountains()
	glColor3f(0,0.7,.6)
	glPointSize(10.0)
	
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glVertex2f(400,0)
	glEnd()
	glutSwapBuffers()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)

	glutInitWindowSize(1000,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("Sunrise")

	glutDisplayFunc(start)
	glutTimerFunc(0,update,0)
	glutIdleFunc(start)
	init()
	glutMainLoop()
main()



