# This program allows a user to SEE THE WIREFEAME CUBE 
# using OpenGL and PyGame.
#
# Version 1.0 - 08.05.22
# 
# Resource 1: https://www.youtube.com/watch?v=R4n4NyDG2hI

import pygame as pg             #import pygame
from pygame.locals import *     #

from OpenGL.GL import *         #import everything from open gl General functions 
from OpenGL.GLU import *        #import everything from open gl advanced functions



# from camera import Camera
# view_cam = Camera()
# WIDTH, HEIGHT = 1280, 720
# last_x, last_y = WIDTH / 2, HEIGHT / 2
# first_mouse = True

# Mouse Look Callback Function...
# def mouse_look(window, x, y):
#     global last_x, last_y

#     if first_mouse:
#         last_x = x
#         last_y = y

#     # Invert axes (OpenGL inverts axes)...
#     x_offset = x - last_x
#     y_offset = last_y - y

#     last_x = x
#     last_y = y

#     view_cam.process_mouse_movement(x_offset, y_offset)

# Mouse Enter Callback Function...
# def mouse_enter(window, entered):
#     global first_mouse

#     if entered:
#         first_mouse = False
#     else:
#         first_mouse = True

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

# def Line():
#     glBegin(GL_LINES)
#     glColor3f(1.0, 1.0, 1.0)
#     glVertex2f(-0.3, -0.5)
#     glVertex2f(0.5, 0.5)
#     glEnd()
# def Line2():
#     glBegin(GL_LINES)
#     glColor3f(1.0, 0.9, 1.0)
#     glVertex2f(0.5, 0.5)
#     glVertex2f(0.5, 0.5)
#     glEnd()

def main():
    # Initialize Display
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef( 0, 0 , 0 ,0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        glRotatef( 1, 3 , 1 ,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube() #render cube 
        pg.display.flip()
        pg.time.wait(10)
main() # Call main Function
                
                
        #     if event.type == pg.MOUSEMOTION:
        #         # Rotate 3D mesh with mouse
        #         if button_down == True:
        #             glRotatef(event.rel[1], 1, 0, 0)
        #             glRotatef(event.rel[0], 0, 1, 0)
        #     # Set the mouse down to true if it has been pressed
        #     for event in pg.mouse.get_pressed():
        #         if pg.mouse.get_pressed()[0] == 1:
        #             button_down = True
        #         elif pg.mouse.get_pressed()[0] == 0:
        #             button_down = False
        
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glMultMatrixf(modelMatrix)
        # modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        # glLoadIdentity()
        # glTranslate(0, 0, -8)
        # glMultMatrixf(modelMatrix)
        # Line2()
        # Line() # Render line 
      
