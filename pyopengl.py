import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pg.init()
windowSize = (1000, 1000)
pg.display.set_mode(display, DOUBLEBUF | OPENGL)