from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *

XTYRES=50
RADIUS=20
FRONT=60
REAR=40
HEIGHT=50
UPLIFT=RADIUS

XMOV=0
OFFSET=0

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)

def makePath():
    glColor3f(1,1,1)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    glVertex2f(-300,0)
    glVertex2f(300,0)
    glEnd()

def makeTyres(xc,yc,r):
    glPointSize(5.0)
    glBegin(GL_TRIANGLE_FAN)
    i=0
    '''while i<=45:
        glColor3f(cos(0.5),cos(0.5),0.8)
        x=RADIUS*cos(OFFSET+radians(i))
        y=RADIUS*sin(OFFSET+radians(i))
        glVertex2f(x+xc,y+yc)
        glVertex2f(-x+xc,y+yc)
        glVertex2f(-x+xc,-y+yc)
        glVertex2f(x+xc,-y+yc)
        glVertex2f(y+xc,x+yc)
        glVertex2f(-y+xc,x+yc)
        glVertex2f(-y+xc,-x+yc)
        glVertex2f(y+xc,-x+yc)
        i=i+1
    glEnd()'''
    while i<=360:
        glColor3f(cos(i),sin(i),cos(i))
        glVertex2f(xc+RADIUS*cos(OFFSET+radians(i)),yc+RADIUS*sin(OFFSET+radians(i)))
        i=i+1
    glEnd()

    

def drawBody():
    glColor3f(0.5,0.8,0.76)
    glBegin(GL_POLYGON)
    glVertex2f(XMOV-XTYRES,HEIGHT+UPLIFT)
    glVertex2f(XMOV+XTYRES,HEIGHT+UPLIFT)
    glVertex2f(XMOV+XTYRES+REAR,RADIUS+UPLIFT)
    glVertex2f(XMOV+XTYRES+FRONT,RADIUS+UPLIFT)
    glVertex2f(XMOV+XTYRES+FRONT,0+UPLIFT)
    glVertex2f(XMOV-(XTYRES+REAR),0+UPLIFT)
    glVertex2f(XMOV-(XTYRES+REAR),RADIUS+UPLIFT)
    glEnd()


def update(x):
    global XMOV,OFFSET
    XMOV=XMOV+1
    OFFSET=OFFSET+2
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),update,int(0))

def plot():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    glColor3f(1,0,1)
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()
    makePath()
    drawBody()
    makeTyres(XMOV+XTYRES,0+UPLIFT,RADIUS)
    makeTyres(XMOV-XTYRES,0+UPLIFT,RADIUS)
    glutSwapBuffers()

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
