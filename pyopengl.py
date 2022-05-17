# This program allows a user to rotate a wireframe mesh with a mouse
# using OpenGL and PyGame.
#
# Version 1.0 - 08.05.22
# 
# Resource 1: https://www.youtube.com/watch?v=R4n4NyDG2hI&t=632s
# Resource 2: https://stackoverflow.com/questions/59823131/how-to-rotate-a-cube-using-mouse-in-pyopengl

import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame_gui

from camera import Camera
view_cam = Camera()
WIDTH, HEIGHT = 1280, 720
last_x, last_y = WIDTH / 2, HEIGHT / 2
first_mouse = True

# Mouse Look Callback Function...
def mouse_look(window, x, y):
    global last_x, last_y

    if first_mouse:
        last_x = x
        last_y = y

    # Invert axes (OpenGL inverts axes)...
    x_offset = x - last_x
    y_offset = last_y - y

    last_x = x
    last_y = y

    view_cam.process_mouse_movement(x_offset, y_offset)

# Mouse Enter Callback Function...
def mouse_enter(window, entered):
    global first_mouse

    if entered:
        first_mouse = False
    else:
        first_mouse = True

# Cube Vertices
vertices = (
    (1, -1, -1), 
    (1, 1, -1), 
    (-1, 1, -1), 
    (-1, -1, -1), #1st
    (1, -1, 1), 
    (1, 1, 1), 
    (-1, -1, 1), 
    (-1, 1, 1) #2nd
)

# Cube Edges
edges = (
    (0, 1), 
    (0, 3), 
    (0, 4), 
    (2, 1), 
    (2, 3), 
    (2, 7), 
    (6, 3), 
    (6, 4), 
    (6, 7), 
    (5, 1), 
    (5, 4), 
    (5, 7)
)
# surfaces = (   #SURFACE COLOURS
#         (0,1,2,3),
#         (3,2,7,6),
#         (6,7,5,4),
#         (4,5,1,0),
#         (1,5,7,2),
#         (4,0,3,6)
# )





def Cube():

    
    
    # Draw Cube
    glBegin(GL_LINES)
    glColor3f(1.0, 0.5, 1.0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Line():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glEnd()

def main():
    # Initialize Display
    pg.init()
    display = (WIDTH, HEIGHT)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    button_down = False

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    while True:
        glPushMatrix()
        glLoadIdentity()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEMOTION:
                # Rotate 3D mesh with mouse
                if button_down == True:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
            
            # Set the mouse down to true if it has been pressed
            for event in pg.mouse.get_pressed():
                if pg.mouse.get_pressed()[0] == 1:
                    button_down = True
                elif pg.mouse.get_pressed()[0] == 0:
                    button_down = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        glTranslate(0, 0, -8)
        glMultMatrixf(modelMatrix)

        Line() # Render cube
        Cube()

        glPopMatrix()

        pg.display.flip()
        pg.time.wait(10)
        

main() # Call main Function
