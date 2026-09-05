import curses
import time
import random
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    my, mx = stdscr.getmaxyx()
    py = my // 2
    px = mx // 2
    score = 0
    floor = my - 3
    frames = 0
    jump = 0
    old_x = 0
    old_y = 0
    oldxx = 0
    oldxy = 0
    xx = 0
    xy = 0
    shot = False
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    mapa = [[0 for i in range(mx)] for j_ in range(my) ]
    block1x = random.randint(3,mx - 3)
    block1y = random.randint(my - 8,my - 3)
    block2x = random.randint(3,mx - 3)
    block2y = random.randint(my // 3,my - 3)
    while True:
        stdscr.erase()
        stdscr.border()
        key = stdscr.getch()
        if key == ord("a"):
            px = max(2, px-1)
        if key == ord("d"):
            px = min(mx-2, px+1)
        if key == ord(" ") and jump < 3:
            py -= 10
            jump += 1
        if key == ord("x"):
            xx = px + 1
            xy = py
            shot = True
        if key == ord("q"):
            return
        if mapa[py+1][px] == 0 and frames != 0:
            py += 1
            frames = 0
        if py == floor -1:
            jump = 0
        mapa[block1y][block1x] = 3
        mapa[block2y][block2x] = 3
        mapa[floor] = [1 for n in range(mx)]
        mapa[py][px] = 2
        mapa[xy][xx] = 4

        for y in range(2,my-2):
            for x in range(2,mx-2):
                try:
                    if mapa[y][x] == 1:
                        stdscr.addstr(y,x, "-")
                    elif mapa[y][x] == 2:
                        stdscr.addstr(y,x, "&")
                    elif mapa[y][x] == 3:
                        stdscr.addstr(y,x, "@")
                    elif mapa[y][x] == 4:
                        stdscr.addstr(y,x, ".")
                except curses.error :
                    pass
        if shot:
            xx += 1
        if mapa[xy][min(xx + 1, mx - 1)] != 0 :
            shot = False
        mapa[oldxy][oldxx] = 0
        mapa[old_y][old_x] = 0
        if xx == mx - 1:
            shot = False
        frames += 1
        oldxx = xx
        oldxy = xy
        old_x = px
        old_y = py
        stdscr.refresh()
        time.sleep(1/30)


curses.wrapper(main)
