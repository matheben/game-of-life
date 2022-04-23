import pygame as pg

pg.display.init()
width = 800
height = 600
cellsize = 10
screen = pg.display.set_mode(size=((width, height)))
white = (255, 255, 255)
black = (0,0,0)
done=False

screen.fill(white)
cells = [[False] * int(width/cellsize) for i in range(int(height/cellsize))]


for i in range(0, width, cellsize):
    pg.draw.line(screen, black, (i, height), (i, 0), width=1)
for i in range(0, height, 10):
    pg.draw.line(screen, black, (width, i), (0, i), width=1)

pg.display.flip()

def drawAlive():
    rPointer = 0
    for r in cells:
        cPointer = 0
        for c in r:
            if c == True:
                pg.draw.rect(screen, black, (cPointer, rPointer, cellsize, cellsize))
            cPointer += 10
        rPointer += 10
    



while not done:

    pg.display.flip()
    drawAlive()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
            #print(pg.mouse.get_pos()[0])
            cells[int(pg.mouse.get_pos()[1]/10)][int(pg.mouse.get_pos()[0]/10)]\
                =not cells[int(pg.mouse.get_pos()[1]/10)][int(pg.mouse.get_pos()[0]/10)]
            

        if event.type == pg.QUIT:
            done=True
            pg.display.flip()

