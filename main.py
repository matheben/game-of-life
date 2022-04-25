import pygame as pg
import pickle

pg.display.init()
filecount = 0
width = 1000
height = 600
cellsize = 10
screen = pg.display.set_mode(size=((width, height)))
white = (255, 255, 255)
black = (0,0,0)
done=False
running = False
cells = [[False] * int(width+10/cellsize) for i in range(int(height+10/cellsize))]



##comment/uncomment to switch to presaved patterns
with open('glider_factory.data', 'rb') as filehandle:
    cells = pickle.load(filehandle)


##Change "teter.txt" to any .txt file in folder and uncomment to load patterns
# file = open('tester.txt')
# fs = file.read()
# r=3
# c=1
# for letter in fs:
#     if letter == "\n":
#         c = 0
#         r+=1
#     if letter == "O":
#         cells[r][c] = True
#     c += 1
# file.close()
##########



def redraw():
    screen.fill(white)
    for i in range(0, width, cellsize):
        pg.draw.line(screen, black, (i, height), (i, 0), width=1)
    for i in range(0, height, 10):
        pg.draw.line(screen, black, (width, i), (0, i), width=1)

def drawAlive():
    rPointer = 0
    for r in cells:
        cPointer = 0
        for c in r:
            if c == True:
                pg.draw.rect(screen, black, (cPointer, rPointer, cellsize, cellsize))
            cPointer += 10
        rPointer += 10
    
def numNeighbors(x, y):
    count = 0
    for c in range(x-1, x+2):
        for r in range(y-1, y+2):
            if(cells[r][c]):
                if not(r == y and c == x):
                    count += 1
    return count

def update():
    kill = []
    revive = []
    for c in range(int(width/10)):
        for r in range(int(height/10)):
            if cells[r][c] and numNeighbors(c, r) < 2:
                kill.append([r, c])
            if cells[r][c] and numNeighbors(c, r) > 3:
                kill.append([r,c])
            if not cells[r][c] and numNeighbors(c, r) == 3:
                revive.append([r, c])
    
    for i in kill:
        cells[i[0]][i[1]] = False
    for i in revive:
        cells[i[0]][i[1]] = True

while not done:
    pg.display.flip()
    redraw()
    if running:
        pg.time.wait(20)
        update()
    drawAlive()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
            cells[int(pg.mouse.get_pos()[1]/10)][int(pg.mouse.get_pos()[0]/10)]\
                = not cells[int(pg.mouse.get_pos()[1]/10)][int(pg.mouse.get_pos()[0]/10)]
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            cells = [[False] * int(width+10/cellsize) for i in range(int(height+10/cellsize))]
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            running = not running
        if event.type == pg.KEYDOWN and event.key == pg.K_c:
            filecount += 1
            with open('my_pattern.data' + str(filecount), 'wb') as filehandle:
                pickle.dump(cells, filehandle)
        if event.type == pg.QUIT:
            done=True

