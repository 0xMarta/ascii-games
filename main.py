import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    #quit = False
    my, mx = stdscr.getmaxyx()
    py = my // 2
    px = mx // 2
    rx = random.randint(1, mx - 3)
    ry = random.randint(1, my - 3)
    score = 0
    dir = 0
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    while True:
        stdscr.border()
        stdscr.erase()
        key = stdscr.getch()
        if key == ord("w"):
            py = max(2, py -1)
            dir = 0
        if key == ord("s"):
            py = min(my-2, py +1)
            dir = 2
        if key == ord("a"):
            px = max(2, px -1)
            dir = 3
        if key == ord("d"):
            px = min(mx-2, px +1)
            dir = 1
        if key == ord("q"):
            return
        try:
            stdscr.addstr(py,px, "●", curses.color_pair(1))
        except curses.error:
            pass
        for i in range(1, score):
            if dir == 0:
                try:
                    stdscr.addstr(py +i,px,"●",curses.color_pair(1))
                except curses.error:
                    pass
            elif dir == 2:
                try:
                    stdscr.addstr(py -i,px,"●",curses.color_pair(1))
                except curses.error:
                    pass
            elif dir == 1:
                try:
                    stdscr.addstr(py,px+i,"●", curses.color_pair(1))
                except curses.error:
                    pass
            elif dir == 3:
                try:
                    stdscr.addstr(py,px-i,"●", curses.color_pair(1))
                except curses.error :
                    pass
        try:
            stdscr.addstr(ry,rx,"o")
        except curses.error :
            pass
        if (py,px) == (ry,rx):
            rx = random.randint(1, mx - 3)
            ry = random.randint(1, my - 3)
            score += 1
        stdscr.refresh()
        time.sleep(1/30)


curses.wrapper(main)
