import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
    display = (1000, 1000)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pg.display.flip()
        pg.time.wait(10)

main()