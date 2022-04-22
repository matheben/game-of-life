import pygame as pg

pg.display.init()
screen = pg.display.set_mode(size=((800, 600)))
white = (255, 255, 255)
black = (0,0,0)
done=False
screen.fill(white)

for i in range(0, 800, 10):
    pg.draw.line(screen, black, (i, 600), (i, 0), width=1)
for i in range(0, 600, 10):
    pg.draw.line(screen, black, (800, i), (0, i), width=1)

pg.display.flip()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done=True
            pg.display.flip()

