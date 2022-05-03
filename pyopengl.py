import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from camera import Camera
view_cam = Camera()
WIDTH, HEIGHT = 1280, 720
last_x, last_y = WIDTH / 2, HEIGHT / 2
first_mouse = True

def mouse_look_clb(window, x, y):
    global last_x, last_y

    if first_mouse:
        last_x = x
        last_y = y

    x_offset = x - last_x
    y_offset = last_y - y

    last_x = x
    last_y = y

    view_cam.process_mouse_movement(x_offset, y_offset)

def mouse_enter_clb(window, entered):
    global first_mouse

    if entered:
        first_mouse = False
    else:
        first_mouse = True

# Cube Vertices
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

# Cube Edges
edges = (
    (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), 
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)

def Cube():
    # Draw Cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
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
                if button_down == True:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
            
            for event in pg.mouse.get_pressed():
                if pg.mouse.get_pressed()[0] == 1:
                    button_down = True
                elif pg.mouse.get_pressed()[0] == 0:
                    button_down = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        glTranslate(0, 0, -5)
        glMultMatrixf(modelMatrix)

        Cube()

        glPopMatrix()

        pg.display.flip()
        pg.time.wait(10)

main()