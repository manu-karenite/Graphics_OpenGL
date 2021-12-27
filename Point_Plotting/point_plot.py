#Program to Plot point at Origin

from OpenGL.GL import *
from OpenGL.GLU import *     #opengl utility library
from OpenGL.GLUT import *    #opengl utility toolkit


def init():
	glClearColor(0.0,0.0,0.0,1.0)		#set background color
	gluOrtho2D(-5.0,5.0,-5.0,5.0)		#set the range of coordinate system

def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)  #clear the entire window to the background color
	glColor3f(1.0,0.0,0.0)			#set color of drawing
	glPointSize(10.0)			#set pixel size
	glBegin(GL_POINTS)
	glVertex2f(0.0,0.0)
	glEnd()
	glFlush()				#push the pixels to display

def main():
	glutInit(sys.argv)			#initialize toolkit
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)	#set display mode
	glutInitWindowSize(500,500)		#set window size
	glutInitWindowPosition(50,50)		#set window position
	glutCreateWindow("Plot Orign")	#create a window with given name
	glutDisplayFunc(plotpoints)		#register redraw function
	init()					#additionalinitilizations
	glutMainLoop()			#call back loop 

main()
