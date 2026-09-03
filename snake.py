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
    snake = [[py,px]]
    rx = random.randint(3, mx - 3)
    ry = random.randint(3, my - 3)
    score = 0
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    def step():
        for j in range(len(snake)-1 , 0 , -1):
            snake[j] = snake[j - 1]
    while True:
        stdscr.erase()
        stdscr.border()
        key = stdscr.getch()
        if key == ord("w"):
            step()
            py = max(1, py -1)
        if key == ord("s"):
            step()
            py = min(my-1, py +1)
        if key == ord("a"):
            step()
            px = max(1, px -1)
        if key == ord("d"):
            step()
            px = min(mx-1, px +1)
        if key == ord("q"):
            return
        try:
            stdscr.addstr(py,px, "●", curses.color_pair(1))
        except curses.error:
             pass
        try:
            stdscr.addstr(ry,rx,"o")
        except curses.error :
            pass
        for k in range(score):
            stdscr.addstr(snake[k][0], snake[k][1], "●", curses.color_pair(1))
        if (py,px) == (ry,rx):
            score += 1
            rx = random.randint(1, mx - 3)
            ry = random.randint(1, my - 3)
            snake.append([])
        snake[0] = [py,px]
        if snake[score-1][0] == my-1 or snake[score-1][1] == mx -1 or snake[score-1][0] == 1 or snake[score-1][1] == 1:
            return
        if score == (mx - 2) * (my - 2) - 20 :
            return
        stdscr.refresh()
        time.sleep(1/30)


curses.wrapper(main)
