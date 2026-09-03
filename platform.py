import curses
import time
import random
import curses
import random
import time

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
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
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
        if key == ord("q"):
            return
        for i in range(3,mx - 3):
            try:
                stdscr.addstr(floor, i, "-")
            except curses.error :
                pass
        try:
            stdscr.addstr(py, px, "&")
        except curses.error:
            pass
        if py < floor - 1 and frames % 2 == 0 :
            py += 1
            frames = 0
        if py == floor -1:
            jump = 0
        frames += 1
        stdscr.refresh()
        time.sleep(1/30)


curses.wrapper(main)
