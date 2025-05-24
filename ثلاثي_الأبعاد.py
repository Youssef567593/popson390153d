from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def عرض_مكعب_ثلاثي():
    def ارسم():
        glBegin(GL_QUADS)
        for سطح in الأوجه:
            for نقطة in سطح:
                glVertex3fv(النقاط[نقطة])
        glEnd()

    النقاط = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    الأوجه = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    pygame.init()
    عرض = (800, 600)
    pygame.display.set_mode(عرض, DOUBLEBUF | OPENGL)
    gluPerspective(45, (عرض[0] / عرض[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for حدث in pygame.event.get():
            if حدث.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        ارسم()
        pygame.display.flip()
        pygame.time.wait(10)
