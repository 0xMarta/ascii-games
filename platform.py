import curses
import time
import random
class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.quit = False
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)
        self.scene = 0
        self.my, self.mx = stdscr.getmaxyx()
        self.py = self.my // 2
        self.px = self.mx // 2
        self.score = 0
        self.test = 0
        self.floor = self.my - 3
        self.frames = 0
        self.jump = 0
        self.hp = 100
        self.enemyx = random.randint(3,self.mx-3)
        self.enemyy = self.my - 8
        self.old_x = 0
        self.old_y = 0
        self.oldxx = 0
        self.oldxy = 0
        self.oldenemyx = 0
        self.oldenemyy = 0
        self.old_leftx = 0
        self.old_lefty = 0
        self.enemy_shotx = 0
        self.enemy_shoty = 0
        self.enemy_shot = False
        self.xx = 0
        self.xy = 0
        self.leftx = 0
        self.lefty = 0
        self.shot = False
        self.leftshot = False
        curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.mapa = [[0 for i in range(self.mx)] for j_ in range(self.my) ]
        self.block1x = random.randint(3,self.mx - 3)
        self.block1y = self.my -3
        self.block2x = random.randint(3,self.mx - 3)
        self.block2y = random.randint(self.my // 3,self.my - 3)
    def scene1(self):
        self.stdscr.erase()
        self.stdscr.border()
        self.stdscr.nodelay(True)
        self.key = self.stdscr.getch()
        if self.key == ord("a") and self.mapa[self.py][self.px-1] == 0:
            self.px = max(2, self.px-1)
        if self.key == ord("d") and self.mapa[self.py][self.px+1] == 0:
            self.px = min(self.mx-2, self.px+1)
        if self.key == ord(" ") and self.jump < 3:
            self.py -= 10
            self.jump += 1
        if self.key == curses.KEY_RIGHT:
            self.xx = self.px + 1
            self.xy = self.py
            self.shot = True
        if self.key == curses.KEY_LEFT:
            self.leftx = self.px - 1
            self.lefty = self.py
            self.leftshot = True
        if self.key == ord("q"):
            self.quit = True
        if self.mapa[self.py+1][self.px] == 0 and self.frames not in [0,1,2]:
            self.py += 1
        if self.enemyy < self.my-1 and self.mapa[self.enemyy+1][self.enemyx] == 0 and self.frames not in [0,1,2]:
            self.enemyy += 1
        if self.py == self.floor -1 or self.mapa[self.py+1][self.px] != 0:
            self.jump = 0
        self.mapa[self.enemyy][self.enemyx] = 5
        self.mapa[self.block1y][self.block1x] = 3
        self.mapa[self.block2y][self.block2x] = 3
        self.mapa[self.floor] = [1 for n in range(self.mx)]
        self.mapa[self.py][self.px] = 2
        self.mapa[self.xy][self.xx] = 4
        self.mapa[self.lefty][self.leftx] = 4

        for y in range(2,self.my-2):
            for x in range(2,self.mx-2):
                try:
                    if self.mapa[y][x] == 1:
                        self.stdscr.addstr(y,x, "-")
                    elif self.mapa[y][x] == 2:
                        self.stdscr.addstr(y,x, "&")
                    elif self.mapa[y][x] == 3:
                        self.stdscr.addstr(y,x, "@")
                    elif self.mapa[y][x] == 4:
                        self.stdscr.addstr(y,x, ".")
                    elif self.mapa[y][x] == 5:
                        self.stdscr.addstr(y,x, "!")

                except curses.error :
                    pass
        if self.shot:
            self.xx += 1
        if self.leftshot:
            self.leftx -=1
        if self.mapa[self.xy][min(self.xx + 1, self.mx - 1)] != 0 :
                self.shot = False
        if self.mapa[self.lefty][max(self.leftx - 1, 3)] != 0 :
            self.leftshot = False
        self.mapa[self.oldxy][self.oldxx] = 0
        self.mapa[self.old_y][self.old_x] = 0
        self.mapa[self.old_lefty][self.old_leftx] = 0
        self.mapa[self.oldenemyy][self.oldenemyx] = 0
        if self.xx == self.mx - 1:
            self.shot = False
        if self.leftx == self.mx - 1:
            self.leftshot = False
        if (self.xx, self.xy) == (self.enemyx, self.enemyy):
            self.mapa[self.xy][self.xx] = 0
            self.score += 1
            self.xx = 0
            self.xy = 0
        if (self.leftx, self.lefty) == (self.enemyx, self.enemyy):
            self.mapa[self.xy][self.xx] = 0
            self.score += 1
            self.leftx = 0
            self.lefty = 0
        self.oldxx = self.xx
        self.oldxy = self.xy
        self.old_x = self.px
        self.old_y = self.py
        self.old_leftx = self.leftx
        self.old_lefty = self.lefty
        self.oldenemyy = self.enemyy
        self.oldenemyx = self.enemyx
        if self.px < self.enemyx and self.frames == 3 and self.mapa[self.enemyy][self.enemyx -1] == 0:
            self.enemyx = min(self.mx-3,self.enemyx - 1 )
        elif self.px > self.enemyx and self.frames == 3 and self.mapa[self.enemyy][self.enemyx +1] == 0:
            self.enemyx = max(3,self.enemyx + 1 )
        if self.mapa[self.enemyy][self.enemyx +1] in [2,3,4] or self.mapa[self.enemyy][self.enemyx -1] in [2,3,4]:
            self.enemyy -= 5
            if self.mapa[self.enemyy][self.enemyx +1] in [2,3,4]:
                self.enemyx = min(self.mx - 2, self.enemyx +1)
                if self.mapa[self.enemyy][self.enemyx -1] in [2,3,4]:
                    self.enemyx = max(2, self.enemyx -1)
        if self.frames == 4:
            self.frames = 0
        self.frames += 1
        try:
            self.stdscr.addstr(self.my - 5,5,f"score: {self.score}")
        except curses.error:
            pass
        try:
            self.stdscr.addstr(self.my - 6,5,f"test: {self.test}")
        except curses.error:
            pass

    def run(self):
        while True:
                self.scene1()
                self.stdscr.refresh()
                time.sleep(1/30)
                if self.quit == True:
                    break

def main(stdscr):
    game = Game(stdscr)
    game.run()

curses.wrapper(main)
