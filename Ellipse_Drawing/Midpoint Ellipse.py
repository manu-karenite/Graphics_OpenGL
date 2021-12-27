from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  #specifies color 
    gluOrtho2D(-100.0,100,-100.0,100) #specifies coordinate axes

def ellipse(xc,yc,rx,ry):
    glColor3f(1.0, 0.4, 0.4)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    #defines the initial points
    x=float(0)
    y=float(ry)

    #calculating everything
    #for region1 
    #initial decision parameter:
    p10=float((ry**2)-(rx*rx*ry)+(0.25*rx*rx))
    dy=float(2*ry*ry*x)
    dx=float(2*rx*rx*y)
    while(dy<dx):
        #what we need to do first? we need to print the values
        glVertex2f(xc+x,yc+y) #1st quadrant
        glVertex2f(xc-x,yc+y) #2nd quadrant
        glVertex2f(xc-x,yc-y) #3rd quadrant
        glVertex2f(xc+x,yc-y) #4th quadrant

        #printing completed now
        #further calculation

        #increment the value fo x for each point in region 1
        x=x+1
        #now we do domething about y
        if(p10<0):
            #no change in y
            dy=dy+(2*ry*ry)
            p10=p10+dy+(ry*ry)
        else:
            #we need to decrement the value of y
            y=y-1
            dy=dy+(2*ry*ry)
            dx=dx-(2*rx*rx)
            p10=p10+dy-dx+(ry*ry)

    #this loop is completed and eventually, the region 1 is completed

    #now we doo for 2nd region
    p20=float(((ry*ry)*(x+0.5)*(x+0.5))+((rx*rx)*(y-1)*(y-1))-(rx*rx*ry*ry))
    while(y>=0):
        #but y has to decrement
        y=y-1
        if(p20>0):
            #no change in x coordinate
            dx=dx-(2*rx*rx)
            p20=p20-dx+(rx*rx)
        else:
            x=x+1
            dx=dx-(2*rx*rx)
            dy=dy+(2*ry*ry)
            p20=p20+dy-dx+(rx*rx)
        #now what? print the points
        glVertex2f(xc+x,yc+y) #1st quadrant
        glVertex2f(xc-x,yc+y) #2nd quadrant
        glVertex2f(xc-x,yc-y) #3rd quadrant
        glVertex2f(xc+x,yc-y) #4th quadrant
    glEnd()
    glFlush()


def main():
    xc=float(input("Enter the x-centre of the ellipse: "))
    yc=float(input("Enter the y-centre of the ellipse: "))
    rx=float(input("Enter the major axis: "))
    ry=float(input("Enter the minor axis: "))

    #defining the open gl functions now
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(2000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("MidPoint Ellipse Generation ALgorithm")
    glutDisplayFunc(lambda: ellipse(xc,yc,rx,ry))
    glutIdleFunc(lambda: ellipse(xc,yc,rx,ry))
    init()
    glutMainLoop()

main() #get to Main Function from here