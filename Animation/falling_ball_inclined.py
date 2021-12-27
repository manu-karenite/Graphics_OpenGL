from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *

RADIUS=40
xc,yc=-500,400
ANIMATE=True
OFFSET=0


def init():
	glClearColor(0,0,0,1)
	gluOrtho2D(-500,500,0,500)

def drawLine():
	glColor3f(1,1,1)
	X1,Y1=-500,400
	X2,Y2=0,0
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glVertex2f(X1,Y1)
	glVertex2f(X2,Y2)
	glEnd()

def drawBall(xc,yc):
	slopeGiven=-0.8
	slopePerpendicular=-1/slopeGiven
	anglePerpendicular=degrees(atan(slopePerpendicular))
	xc=xc+RADIUS*cos(radians(anglePerpendicular))
	yc=yc+RADIUS*sin(radians(anglePerpendicular))
	
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(xc,yc)
	i=0
	while i<=360:
		glColor3f(cos(i),sin(i),cos(i))
		glVertex2f(xc+RADIUS*cos(OFFSET+radians(i)),yc+RADIUS*sin(OFFSET+radians(i)))
		i=i+1
	glEnd()

	

def plot():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,1,1)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	glEnd()
	
	drawBall(xc,yc)
	drawLine()
	glutSwapBuffers()

def update(x):
	global xc,yc,ANIMATE,OFFSET
	if ANIMATE==True:
		yc=yc-1
		xc=(-5*yc)/4
		OFFSET=OFFSET+2
	if yc<=10:
		ANIMATE=False


	if ANIMATE==False:
		xc=int(xc+2)
		OFFSET=OFFSET-2
	if xc+66>500:
		return
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(500,500)
	glutCreateWindow("Falling Ball")
	glutDisplayFunc(plot)
	glutTimerFunc(0,update,0)
	init()
	glutMainLoop()
main()