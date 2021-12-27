from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
from time import *
from datetime import datetime
import pytz

curr=datetime.now(pytz.timezone('Asia/Kolkata'))
hrs=curr.hour
mins=curr.minute
secs=curr.second


LEN=50
FULL=100
def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-500,500,-500,500)

def drawSegment(xc,yc,num):
	#arr=getArray(num)
	arr=[]
	if num==0:
		arr=[1,1,1,0,1,1,1]
	elif num==1:
		arr=[0,0,1,0,0,1,0]
	elif num==2:
		arr=[1,0,1,1,1,0,1]
	elif num==3:
		arr=[1,0,1,1,0,1,1]
	elif num==4:
		arr=[0,1,1,1,0,1,0]
	elif num==5:
		arr=[1,1,0,1,0,1,1]
	elif num==6:
		arr=[1,1,0,1,1,1,1]
	elif num==7:
		arr=[1,0,1,0,0,1,0]
	elif num==8:
		arr=[1,1,1,1,1,1,1]
	elif num==9:
		arr=[1,1,1,1,0,1,1]
	#return arr

	glLineWidth(10.0)
	glColor3f(1,0,0)
	
	if arr[0]==1:
		glBegin(GL_LINES)
		glVertex2f(xc-LEN,yc+FULL)
		glVertex2f(xc+LEN,yc+FULL)
		glEnd()

	if arr[1]==1:
		glBegin(GL_LINES)
		glVertex2f(xc-LEN,yc)
		glVertex2f(xc-LEN,yc+FULL)
		glEnd()

	if arr[2]==1:
		glBegin(GL_LINES)
		glVertex2f(xc+LEN,yc+FULL)
		glVertex2f(xc+LEN,yc)
		glEnd()

	if arr[3]==1:
		glBegin(GL_LINES)
		glVertex2f(xc-LEN,yc)
		glVertex2f(xc+LEN,yc)
		glEnd()

	if arr[4]==1:	
		glBegin(GL_LINES)
		glVertex2f(xc-LEN,yc-FULL)
		glVertex2f(xc-LEN,yc)
		glEnd()

	if arr[5]==1:
		glBegin(GL_LINES)
		glVertex2f(xc+LEN,yc)
		glVertex2f(xc+LEN,yc-FULL)
		glEnd()

	if arr[6]==1:
		glBegin(GL_LINES)
		glVertex2f(xc+LEN,yc-FULL)
		glVertex2f(xc-LEN,yc-FULL)
		glEnd()



def drawColon(x):
    sleep(0.2)
    glPointSize(15.0)
    glColor3f(1,1,0)
    glBegin(GL_POINTS)
    glVertex2f(x,50)
    glVertex2f(x,-50)
    glEnd()

def plot():

    glClear(GL_COLOR_BUFFER_BIT)
    hourfirst=int(hrs/10)
    hoursecond=hrs%10

    minutefirst=int(mins/10)
    minutesecond=mins%10

    secondfirst=int(secs/10)
    secondsecond=secs%10



    print(hourfirst)
    print(hoursecond)
    print(minutefirst)
    print(minutesecond)
    drawSegment(-365,0,hourfirst)
    drawSegment(-235,0,hoursecond)
    drawSegment(-65,0,minutefirst)
    drawSegment(65,0,minutesecond)
    drawSegment(235,0,secondfirst)
    drawSegment(365,0,secondsecond)
    drawColon(150)
    drawColon(-150)
    glFlush()


def update(x):
	global curr,hrs,mins,secs
	curr=datetime.now(pytz.timezone('Asia/Kolkata'))
	hrs=curr.hour
	mins=curr.minute
	secs=curr.second
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,int(0))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("Digital Clock")
    glutDisplayFunc(plot)
    glutTimerFunc(0,update,0)
    init()
    glutMainLoop()
main()
