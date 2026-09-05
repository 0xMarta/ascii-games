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
    enemyx = random.randint(3,mx-3)
    enemyy = my - 8
    old_x = 0
    old_y = 0
    oldxx = 0
    oldxy = 0
    oldenemyx = 0
    oldenemyy = 0
    old_leftx = 0
    old_lefty = 0
    xx = 0
    xy = 0
    leftx = 0
    lefty = 0
    shot = False
    leftshot = False
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    mapa = [[0 for i in range(mx)] for j_ in range(my) ]
    block1x = random.randint(3,mx - 3)
    block1y = my -3  #random.randint(my - 8,my - 3)
    block2x = random.randint(3,mx - 3)
    block2y = random.randint(my // 3,my - 3)
    while True:
        stdscr.erase()
        stdscr.border()
        key = stdscr.getch()
        if key == ord("a") and mapa[py][px-1] == 0:
            px = max(2, px-1)
        if key == ord("d") and mapa[py][px+1] == 0:
            px = min(mx-2, px+1)
        if key == ord(" ") and jump < 3:
            py -= 10
            jump += 1
        if key == curses.KEY_RIGHT:
            xx = px + 1
            xy = py
            shot = True
        if key == curses.KEY_LEFT:
            leftx = px - 1
            lefty = py
            leftshot = True
        if key == ord("q"):
            return
        if mapa[py+1][px] == 0 and frames not in [0,1,2]:
            py += 1
        if enemyy < my-1 and mapa[enemyy+1][enemyx] == 0 and frames not in [0,1,2]:
            enemyy += 1
        if py == floor -1 or mapa[py+1][px] != 0:
            jump = 0
        mapa[enemyy][enemyx] = 5
        mapa[block1y][block1x] = 3
        mapa[block2y][block2x] = 3
        mapa[floor] = [1 for n in range(mx)]
        mapa[py][px] = 2
        mapa[xy][xx] = 4
        mapa[lefty][leftx] = 4

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
                    elif mapa[y][x] == 5:
                        stdscr.addstr(y,x, "!")
                except curses.error :
                    pass
        if shot:
            xx += 1
        if leftshot:
            leftx -=1
        if mapa[xy][min(xx + 1, mx - 1)] != 0 :
            shot = False
        if mapa[lefty][max(leftx - 1, 3)] != 0 :
            leftshot = False
        mapa[oldxy][oldxx] = 0
        mapa[old_y][old_x] = 0
        mapa[old_lefty][old_leftx] = 0
        mapa[oldenemyy][oldenemyx] = 0
        if xx == mx - 1:
            shot = False
        if leftx == mx - 1:
            leftshot = False
        if (xx, xy) == (enemyx, enemyy):
            mapa[xy][xx] == 0
            score += 1
            xx = 0
            yy = 0
        if (leftx, lefty) == (enemyx, enemyy):
            mapa[xy][xx] == 0
            score += 1
            leftx = 0
            lefty = 0
        oldxx = xx
        oldxy = xy
        old_x = px
        old_y = py
        old_leftx = leftx
        old_lefty = lefty
        oldenemyy = enemyy
        oldenemyx = enemyx
        if px < enemyx and frames == 3 and mapa[enemyy][enemyx -1] == 0:
            enemyx = min(mx-3,enemyx - 1 )
        elif px > enemyx and frames == 3 and mapa[enemyy][enemyx +1] == 0:
            enemyx = max(3,enemyx + 1 )
        if mapa[enemyy][enemyx +1] in [2,3,4] or mapa[enemyy][enemyx -1] in [2,3,4]:
            enemyy -= 5
            if mapa[enemyy][enemyx +1] in [2,3,4]:
                enemyx = min(mx - 2, enemyx +1)
            if mapa[enemyy][enemyx -1] in [2,3,4]:
                enemyx = max(2, enemyx -1)

        if frames == 4:
            frames = 0
        frames += 1
        try:
            stdscr.addstr(my - 5,5,f"score: {score}")
        except curses.error:
            pass
        stdscr.refresh()
        time.sleep(1/30)


curses.wrapper(main)
