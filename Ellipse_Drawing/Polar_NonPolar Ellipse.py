from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
import math
import sys


def ROUND(a):
	return int(a+0.4)

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	gluOrtho2D(-150.0, 150.0, -150.0, 150.0)
# Setting pixel
def setPixel(xcoordinate,ycoordinate):
	glColor3f(1.0,0.5,0.8)
	glPointSize(5.0)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(0,-500)
	glVertex2f(0,500)
	glEnd()
	glColor3f(0.8,0.2,0.9)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def polarEllipse(x_centre,y_centre,x_radius,y_radius):
	theta = 0
	theta_end = 2*math.pi
	while(theta <= theta_end):
		x = x_radius*(math.cos(theta)) + x_centre
		y = y_radius*(math.sin(theta)) + y_centre
		setPixel(ROUND(x + x_centre),ROUND(y + y_centre))
		theta += 0.001


def nonpolarEllipse(x_centre,y_centre,x_radius,y_radius):
	x = -x_radius
	b = y_radius
	a = x_radius
	v = 1-((x/a)*(x/a))
	while x < 0:
		y = b* (math.sqrt(1-((x/a)*(x/a))))
		setPixel(ROUND(x + x_centre),ROUND(y + y_centre))
		setPixel(ROUND(-x + x_centre), ROUND(y + y_centre))
		setPixel(ROUND(-x + x_centre), ROUND(-y + y_centre))
		setPixel(ROUND(x + x_centre), ROUND(-y + y_centre))
		x += 0.01

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	if option == 1:
		polarEllipse(x_centre,y_centre,x_radius,y_radius)
	elif option == 2:
		nonpolarEllipse(x_centre,y_centre,x_radius,y_radius)
	else:
		print('Invalid input')
		exit()

def main():
	global x_centre,y_centre,x_radius,y_radius, option
	option = int(input('\nPlease Choose\n\t1. Polar\n\t2. Non-Polar\n'))
	print("Center Coordinates (x,y)")
	x_centre=int(input('x:'))
	y_centre=int(input('y:'))
	x_radius=int(input('x-axis Radius: '))
	y_radius = int(input('y-axis Radius: '))
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow('Ellipse Drawing Algo')
	glutDisplayFunc(display)
	init()
	glutMainLoop()

main()