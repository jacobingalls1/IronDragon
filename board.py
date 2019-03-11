import pygame

SCALE = .5


class CellDescriptor(object):
    def __init__(self, name, icon, baseCost):
        self.name = name
        self.icon = pygame.transform.scale(icon, (int(SCALE*icon.get_width()), int(SCALE*icon.get_height())))
        self.cost = baseCost


class BoardCell(object):
    def __init__(self, posX, posY, symbol, cell):
        self.posX = posX
        self.posY = posY
        self.symbol = symbol
        self.cell = cell

    def pos(self, x=1, y=1):
        return [(self.posX + .5) * x, (self.posY + .5) * y]


class Board(object):
    def __init__(self):
        self._board = []
        self._legend = {}
        self._adjacencies = {}

    def setup(self, initDir):
        legend = open(initDir + '/legend.txt', 'r')
        for line in legend:
            line = line.split(':')
            self._legend[line[0]] = line[1]
        self._map = pygame.image.load(initDir + '/map.png')
        for i in self._legend.keys():
            self._legend[i] = CellDescriptor(self._legend[i], pygame.image.load(initDir + '/Terrain/' + self._legend[i].split(',')[0] + '.png'), self._legend[i].split(',')[1])
        map = open(initDir + '/map.csv')
        i = 0
        for line in map:
            currLine = []
            line = line.split(',')
            for j in range(len(line)):
                currLine.append(BoardCell(i, j, line[j].split()[0], self._legend[line[j].split()[0]]))
            self._board.append(currLine)
            i += 1

    def getBoard(self):
        return self._board

    def getLegend(self):
        return self._legend

    def getMap(self):
        return self._map

    def doAdjacencies(self, hex=False):
        if hex:
            for row in self._board:
                for cell in row:
                    adj = []
                    if cell.posX != 0:
                        adj.append([self._board[cell.posX - 1][cell.posY], -1])
                    if cell.posX != len(self._board[0]) - 1:
                        adj.append([self._board[cell.posX + 1][cell.posY], -1])
                    if cell.posY != len(self._board) - 1:
                        adj.append([self._board[cell.posX][cell.posY + 1], -1])
                        if cell.posX != 0 and cell.posY%2 == 0:
                            adj.append([self._board[cell.posX - 1][cell.posY + 1], -1])
                    if cell.posY != len(self._board) - 1:
                        adj.append([self._board[cell.posX][cell.posY + 1], -1])
                        if cell.posX != len(self._board[0]) - 1 and cell.posY%2 == 1:
                            adj.append([self._board[cell.posX + 1][cell.posY + 1], -1])
                    self._adjacencies[cell] = adj
        else:
            for row in self._board:
                for cell in row:
                    adj = []
                    if cell.posX != 0:
                        adj.append([self._board[cell.posX - 1][cell.posY], -1])
                    if cell.posY != 0:
                        adj.append([self._board[cell.posX][cell.posY - 1], -1])
                    if cell.posX != len(self._board[0]) - 1:
                        adj.append([self._board[cell.posX + 1][cell.posY], -1])
                    if cell.posY != len(self._board) - 1:
                        adj.append([self._board[cell.posX][cell.posY + 1], -1])
                    self._adjacencies[cell] = adj

    def getAdjacencies(self):
        return self._adjacencies




