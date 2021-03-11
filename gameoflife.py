#!/usr/bin/env python3
import time
import curses
import random

def main(window):

    art = '▓'
    sleep = 0.001
    k = 1
    h, w = window.getmaxyx()
    h -= 1
    w -= 1

    # Seed
    world = [[1 if random.random() > k else 0 for _ in range(w)] for __ in range(h)]

    world[5][1] = 1
    world[5][2] = 1
    world[6][1] = 1
    world[6][2] = 1

    world[5][11] = 1
    world[6][11] = 1
    world[7][11] = 1
    world[4][12] = 1
    world[8][12] = 1
    world[3][13] = 1
    world[9][13] = 1
    world[3][14] = 1
    world[9][14] = 1
    world[6][15] = 1
    world[4][16] = 1
    world[8][16] = 1
    world[5][17] = 1
    world[6][17] = 1
    world[7][17] = 1
    world[6][18] = 1

    world[3][21] = 1
    world[4][21] = 1
    world[5][21] = 1
    world[3][22] = 1
    world[4][22] = 1
    world[5][22] = 1
    world[2][23] = 1
    world[6][23] = 1
    world[1][25] = 1
    world[2][25] = 1
    world[6][25] = 1
    world[7][25] = 1

    world[4][35] = 1
    world[5][35] = 1
    world[4][36] = 1
    world[5][36] = 1

    world = [[1 if random.random() > 0.5 else 0 for _ in range(w)] for __ in range(h)]

    try:
        while True:

            for i, line in enumerate(world):
                linestr = ''.join(map(str, line))
                linestr = linestr.replace('0', ' ').replace('1', art)
                window.addstr(i, 0, linestr)
            window.refresh()
            time.sleep(sleep)

            nextworld = [[0 for _ in range(w)] for __ in range(h)]
            for i in range(h):
                for j in range(w):
                    iadjs = [i+di for di in [-1, 0, 1] if i+di >= 0 and i+di < h]
                    jadjs = [j+dj for dj in [-1, 0, 1] if j+dj >= 0 and j+dj < w]
                    adjs = [world[iadj][jadj] for iadj in iadjs for jadj in jadjs if not (iadj == i and jadj == j)]
                    nadjs = sum(adjs)

                    if nadjs == 3 or (world[i][j] and nadjs == 2):
                        nextworld[i][j] = 1
            world = nextworld

    except KeyboardInterrupt:
        pass

curses.wrapper(main)
