from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *

ANGLE_MAX=35
ANGLE_MIN=-35
ANGLE=0
LENGTH=400

#for vertical
VX1=300
VY1=0

VX2=300
VY2=50

#FOR HORIZONTAL
HX1=250
HY1=50

HX2=350
HY2=50

UP=True

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-500,500,-500,500)

def drawLine():
	glColor3f(0.2,1,0.5)
	glLineWidth(8.0)
	glBegin(GL_LINES)
	glVertex2f(LENGTH*cos(radians(ANGLE)),LENGTH*sin(radians(ANGLE)))
	glVertex2f(LENGTH*cos(radians(180+ANGLE)),LENGTH*sin(radians(180+ANGLE)))
	glEnd()

def drawHandles():
	global VX1,VY1,VX2,VY2,HX1,HY1,HX2,HY2
	#for vertical

	X1=VX1*cos(radians(ANGLE))-VY1*sin(radians(ANGLE))
	Y1=VX1*sin(radians(ANGLE))+VY1*cos(radians(ANGLE))

	X2=VX2*cos(radians(ANGLE))-VY2*sin(radians(ANGLE))
	Y2=VX2*sin(radians(ANGLE))+VY2*cos(radians(ANGLE))

	#FOR HORIZONTAL
	X3=HX1*cos(radians(ANGLE))-HY1*sin(radians(ANGLE))
	Y3=HX1*sin(radians(ANGLE))+HY1*cos(radians(ANGLE))

	X4=HX2*cos(radians(ANGLE))-HY2*sin(radians(ANGLE))
	Y4=HX2*sin(radians(ANGLE))+HY2*cos(radians(ANGLE))

	glColor3f(0.2,0.7,0.5)
	glBegin(GL_LINES)
	glVertex2f(X1,Y1)
	glVertex2f(X2,Y2)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(X3,Y3)
	glVertex2f(X4,Y4)
	glEnd()

	VX1BAR=-VX1
	VX2BAR=-VX2
	HX1BAR=-HX1
	HX2BAR=-HX2

	X1=VX1BAR*cos(radians(ANGLE))-VY1*sin(radians(ANGLE))
	Y1=VX1BAR*sin(radians(ANGLE))+VY1*cos(radians(ANGLE))

	X2=VX2BAR*cos(radians(ANGLE))-VY2*sin(radians(ANGLE))
	Y2=VX2BAR*sin(radians(ANGLE))+VY2*cos(radians(ANGLE))

	#FOR HORIZONTAL
	X3=HX1BAR*cos(radians(ANGLE))-HY1*sin(radians(ANGLE))
	Y3=HX1BAR*sin(radians(ANGLE))+HY1*cos(radians(ANGLE))

	X4=HX2BAR*cos(radians(ANGLE))-HY2*sin(radians(ANGLE))
	Y4=HX2BAR*sin(radians(ANGLE))+HY2*cos(radians(ANGLE))

	glBegin(GL_LINES)
	glVertex2f(X1,Y1)
	glVertex2f(X2,Y2)
	glEnd()

	glBegin(GL_LINES)
	glVertex2f(X3,Y3)
	glVertex2f(X4,Y4)
	glEnd()
	

def drawHinge():
	glColor3f(0.5,0.6,0.2)
	glBegin(GL_POLYGON)
	glVertex2f(0,0)
	glVertex2f(-50,-50)
	glVertex2f(50,-50)
	glEnd()





def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	glPointSize(10.0)
	
	drawHinge()
	drawHandles()
	drawLine()
	glFlush()

def update(x):
	global ANGLE,UP
	if UP==True:
		if ANGLE<ANGLE_MAX:
			ANGLE=ANGLE+0.5
		elif ANGLE==ANGLE_MAX:
			UP=False
	elif UP==False:
		if ANGLE>ANGLE_MIN:
			ANGLE=ANGLE-0.5
		elif ANGLE==ANGLE_MIN:
			UP=True

	
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(500,500)
    glutCreateWindow("Gaadi")
    glutDisplayFunc(plot)
    glutTimerFunc(0,update,0)
    init()
    glutMainLoop()
main()
