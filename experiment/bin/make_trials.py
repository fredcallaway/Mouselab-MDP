#!/usr/bin/env python3
"""Generates trials json for the demo experiment."""

import json
import random

def emoji():
    return random.choice('😀😃😄😁😆😅😂️😊😇🙂🙃😉😌😍😘😗😙😚😋😜😝😛🤑🤗🤓😎')

def grid(size):
    
    graph = {}
    layout = {}

    def reward():
        return random.randint(-9, 10)
    
    def state(x, y):
        name = '{}_{}'.format(x, y)
        if name in graph:
            return name

        graph[name] = {}
        layout[name] = [x, y]
        if y < size:
            graph[name]['down'] = [reward(), state(x, y+1)]
        if x < size:
            graph[name]['right'] = [reward(), state(x+1, y)]
        return name

    state(0, 0)

    return {
        'stateLabels': {s: emoji() for s in layout},
        'graph': graph,
        'layout': layout,
        'initial': '0_0',
    }

def grid_trials():
    yield {
        **grid(2),
        'centerMessage': '<b>Hover rewards</b>',
        'edgeDisplay': 'hover',
        'playerImage': 'static/images/oski.png',
        'playerImageScale': 0.1
    }
    yield {
        **grid(3),
        'centerMessage': '<b>Clickable states</b>',
        'edgeDisplay': False,
        'stateDisplay': 'click',
        'playerImage': 'static/images/spider.png'
    }
    yield {
        'centerMessage': '<b>Fully observable</b>',
        **grid(2),
    }

def fancy_trials():
    graph, layout = build('heart', size=2)
    yield {
        'graph': graph,
        'layout': layout,
        # 'stateLabels': dict(zip(graph.keys(), graph.keys())),
        'playerImageScale': 0.2,
        'size': 90,
        # 'stateRewards': {k: random.randint(-9, 9) for k in graph},
        # 'stateLabels': 'reward',
        'stateDisplay': 'click',
        'edgeDisplay': 'never',
        'initial': '0'
    }


def main():

    # trials = list(grid_trials())
    trials = list(grid_trials())
    outfile = 'static/json/trials.json'
    with open(outfile, 'w+') as f:
        json.dump(trials, f)

    print('wrote {} trials to {}'.format(len(trials), outfile))



import numpy as np
import itertools as it
from scipy.io import savemat
import os
import json
from collections import defaultdict

from toolz import *

# ---------- Constructing environments ---------- #
DIRECTIONS = ('up', 'right', 'down', 'left')
ACTIONS = dict(zip(DIRECTIONS, it.count()))


BRANCH_DIRS = {
    2: {'up': ('right', 'left'),
        'right': ('up', 'down'),
        'down': ('right', 'left'),
        'left': ('up', 'down'),
        'all': ('right', 'left')},
    3: {'up': ('up', 'right', 'left'),
        'right': ('up', 'right', 'down'),
        'down': ('right', 'down', 'left'),
        'left': ('up', 'down', 'left'),
        'all': DIRECTIONS}
}

def move_xy(x, y, direction, dist=1):
    return {
        'right': (x+dist, y),
        'left': (x-dist, y),
        'down': (x, y+dist),
        'up': (x, y-dist),
    }.get(direction)



    
class Layouts:

    def cross(depth):
        graph = {}
        layout = {}
        names = it.count()

        def direct(prev):
            if prev == 'all':
                yield from DIRECTIONS
            else:
                yield prev
        
        def node(d, x, y, prev_dir):
            r = 0  # reward is 0 for now
            name = str(next(names))
            layout[name] = (x, y)
            graph[name] = {}
            if d > 0:
                for direction in direct(prev_dir):
                    x1, y1 = move_xy(x, y, direction, 1)
                    graph[name][direction] = (r, node(d-1, x1, y1, direction))
                                            
            return name
        
        node(depth, 0, 0, 'all')
        return graph, layout


    def tree(branch, depth, first='up', **kwargs):
        graph = {}
        layout = {}
        names = it.count()

        def dist(d):
            if branch == 3:
                return 2 ** (d - 1)
            else:
                return 2 ** (d/2 - 0.5)

        def node(d, x, y, prev_dir):
            r = 0  # reward is 0 for now
            name = str(next(names))
            layout[name] = (x, y)
            graph[name] = {}
            if d > 0:
                for direction in BRANCH_DIRS[branch][prev_dir]:
                    x1, y1 = move_xy(x, y, direction, dist(branch, d))
                    graph[name][direction] = (r, node(d-1, x1, y1, direction))
                                            
            return name

        node(depth, 0, 0, first)
        return graph, layout


    def heart(size):
        last_full = (size + 1)* 2

        def layer(h):            

            def full():
                x_max = 0.5 * h
                x = -x_max
                while x < x_max:
                    yield (x, h)
                    x += 1
            
            skip = h - last_full
            keep = size + 1 - skip
            if skip <= 0:
                yield from full()
            else:
                lay = drop(skip, full())
                yield from take(keep, lay)
                lay = drop(skip, lay)
                yield from take(keep, lay)

        all_nodes = concat(layer(h) for h in range(1, 3 * size + 3))
        layout = dict(zip(it.count(), all_nodes))
        r_layout = {v: k for k, v in layout.items()}

        graph = {n: {} for n in layout}
        for n, (x, y) in layout.items():
            left = r_layout.get((x - 0.5, y + 1))
            if left:
                graph[n]['left'] = (0, left)
            right = r_layout.get((x + 0.5, y + 1))
            if right:
                graph[n]['right'] = (0, right)

        return graph, layout


def rescale(layout):
    names, xy = zip(*layout.items())
    x, y = np.array(list(xy)).T
    y *= -1
    x -= x.min()
    y -= y.min()
    y *= 0.5
    x *= 1.5
    return dict(zip(names, zip(x.tolist(), y.tolist())))


def build(kind, **kwargs):
    graph, layout = getattr(Layouts, kind)(**kwargs)
    return graph, rescale(layout)



if __name__ == '__main__':
    main()
    # s = Stims().run()
