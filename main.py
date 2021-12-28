import pygame as pg
import setings as st
from sys import exit


def main():

#====================================================INIT====================================================
# Pygame init
    pg.init()
    screen = pg.display.set_mode(st.WINDOW_SIZE)
    screen.fill(st.WINDOW_BACKGROUND)
    pg.display.set_caption(st.GAME_NAME)
    clock = pg.time.Clock()
# Game init
    AREA_POS_X = st.GAME_AREA_PADDING_X
    AREA_POS_Y = st.GAME_AREA_PADDING_Y
    AREA_HIGHT = st.WINDOW_HEIGHT - (AREA_POS_Y + 10)
    AREA_WIDTH = st.WINDOW_WIDTH - (AREA_POS_X + 10)


    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                return
        clock.tick(st.GAME_FPS)
        pg.display.update()
        screen.fill(st.WINDOW_BACKGROUND)
        pg.draw.rect(screen, st.GAME_AREA_COLOR, (AREA_POS_X, AREA_POS_Y, AREA_WIDTH, AREA_HIGHT))
        pg.display.update()



if __name__ == '__main__':
    main()