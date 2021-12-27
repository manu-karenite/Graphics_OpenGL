from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
from time import sleep
XC=-460
YC=120
RADIUS=20
RIGHT=True
ANGLE=30
LEG=40/cos(radians(30))

THETA1=-60
THETA2=-120

THETA=60
def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-500,500,-50,500)


def drawFace(xc,yc,RADIUS):
	glColor3f(0.4,0.5,0.66)
	glPointSize(2.0)
	i=0
	glBegin(GL_POINTS)
	while i<=45:
		x=RADIUS*cos(radians(i))
		y=RADIUS*sin(radians(i))
		glVertex2f(x+xc,y+yc)
		glVertex2f(-x+xc,y+yc)
		glVertex2f(-x+xc,-y+yc)
		glVertex2f(x+xc,-y+yc)
		glVertex2f(y+xc,x+yc)
		glVertex2f(-y+xc,x+yc)
		glVertex2f(-y+xc,-x+yc)
		glVertex2f(y+xc,-x+yc)
		i=i+1
	glEnd()

def drawMan():
	glColor3f(0.5,0.78,0.34)
	glLineWidth(2.5)
	glBegin(GL_LINES)
	glVertex2f(XC,40)
	glVertex2f(XC,100)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(XC+40,75)
	glVertex2f(XC-40,75)
	glEnd()
	drawFace(XC,YC,RADIUS)



def drawFloor():
	glColor3f(1,1,1)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()

def drawLegs():


	glLineWidth(7.5)
	glColor3f(.51,.19,.81)
	glBegin(GL_LINES)
	glVertex2f(XC,40)
	glVertex2f(XC+LEG*cos(radians(THETA1)),40+LEG*sin(radians(THETA1)))
	glEnd()
	glColor3f(.89,.4,.81)
	glBegin(GL_LINES)
	glVertex2f(XC,40)
	glVertex2f(XC+LEG*cos(radians(THETA2)),40+LEG*sin(radians(THETA2)))
	glEnd()


def update(x):
	sleep(0.5)
	global XC,RIGHT,THETA1,THETA2
	if RIGHT==True:
		if (XC+40)<500:
			XC=XC+50
		else:
			RIGHT=False
	elif RIGHT==False:
		if (XC-40)>-500:
			XC=XC-50
		else:
			RIGHT=True
	if THETA1==-60:
		THETA1=-120
		THETA2=-60
	elif THETA1==-120:
		THETA1=-60
		THETA2=-120

	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))	

def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(10.0)
	drawFloor()
	drawMan()
	drawLegs()
	glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(500,500)
    glutCreateWindow("Man")
    glutDisplayFunc(plot)
    glutTimerFunc(0,update,0)
    init()
    glutMainLoop()
main()