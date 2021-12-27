from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
import numpy


RADIUS=150
XC=0
YC=0
XF=-400
YF=0
RB=20
START=True
ANGLE=180
xcoord=[]
ycoord=[]



def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,-500,500)

def createFloor():
	glColor3f(0.6,0,0.8)
	glLineWidth(1.0)
	glBegin(GL_LINES)
	glVertex2f(-500,-20)
	glVertex2f(500,-20)
	glEnd()

def createPath():
	glColor3f(1,1,0)
	glPointSize(2.5)
	lenth=len(xcoord)
	glBegin(GL_POINTS)
	i=0
	while i<lenth:
		glVertex2f(xcoord[i],ycoord[i])
		i=i+250
	glEnd()
def bounce():

	glClear(GL_COLOR_BUFFER_BIT)
	createPath()
	glColor3f(1,0,0.6)
	glPointSize(5.0)
	XC=XF+RADIUS*cos(radians(ANGLE))
	YC=YF+RADIUS*sin(radians(ANGLE))
	xcoord.append(XC)
	ycoord.append(YC)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(XC,YC)
	

	i=0
	while i<=360:
		glVertex2f(XC+RB*cos(radians(i)),YC+RB*sin(radians(i)))
		i=i+1
	glEnd()
	createFloor()

	glutSwapBuffers()


	

def redraw(x):
	global ANGLE,XF,RADIUS
	if ANGLE>0:
		ANGLE=ANGLE-1
	elif ANGLE==0:
		ANGLE=180
		XF=XF+RADIUS
		RADIUS=RADIUS*0.8
		XF=XF+RADIUS		
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),redraw,int(0))

def main():

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Moving Fan")
	
	glutDisplayFunc(bounce)
	glutTimerFunc(0,redraw,0)
	glutIdleFunc(bounce)
	init()
	glutMainLoop()
main()