import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
w,h = 500,500

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (-500.0, 500.0, -500.0, 500.0)

def midPoint(X1,Y1,X2,Y2):  
    # calculate dx & dy  
    dx = X2 - X1  
    dy = Y2 - Y1  
  
    # initial value of decision parameter d  
    d = dy - (dx/2)  
    x = X1 
    y = Y1  
  
    # Plot initial given point  
    # putpixel(x,y) can be used to print pixel  
    # of line in graphics  
    print(x,",",y,"\n") 
    # iterate through value of X 
    i = 0 
    while (x < X2): 
        x=x+1
        
        if(d < 0): 
            d = d + dy  
  
      
        else: 
            d = d + (dy - dx)  
            y=y+1
        
        X[i] = x
        Y[i] = y
        i = i + 1
  
        # Plot intermediate points  
        # putpixel(x,y) is used to print pixel  
        # of line in graphics    
  
def plotDDA():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for i in range(length):
        glVertex2i(X[i],Y[i])    
    glEnd()
    glFlush()
        

a,b,c,d = [int(a) for a in input("Enter x1 y1 and x2 y2 value: ").split()]
global length 
length = (c-a) if (c-a) > (d-b) else (d-b)
X = [0] * length
Y = [0] * length
midPoint(a,b,c,d)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(100,100)
glutCreateWindow(b'Line using Mid-point Algorithm')
init2D(0.0,0.0,0.0)
glutDisplayFunc(plotDDA)
glutMainLoop()