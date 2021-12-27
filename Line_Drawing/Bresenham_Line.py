from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0) #origin at left bottom
def plotLine(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)

    #we first need to plot the given x1,y1
    glVertex2f(x1,y1);

    #we calculate initial decision parameter
    if deltaX>deltaY:
        #case 1
        p = 2*deltaY - deltaX;
        while x1<x2:
            x1=x1+1
            if p<0:
                p=p+2*deltaY
            else:
                y1=y1+1
                p=p+2*(deltaY-deltaX)
            glVertex2f(x1,y1);


    else:
        #case 2
        p=2*deltaX-deltaY
        while y1<y2:
            y1=y1+1
            if p<0:
                p=p+2*deltaX
            else:
                x1=x1+1
                p=p+2*(deltaX-deltaY)
            glVertex2f(x1,y1);
    glEnd()
    glFlush()


def main():
    print ("Enter following coordinates for a line :")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Plot Line using Bressehnham Algorithm")
    glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2))
    init()
    glutMainLoop()
main()