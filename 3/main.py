class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ',' + str(self.y)


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = dict()

        for x in range(0, width):
            for y in range(0, height):
                self.grid[(x, y)] = Node(x, y)

    def __str__(self):
            for y in reversed(range(self.height)):
                print([str(self.grid[(x, y)]) for x in range(self.width)])


g = Grid(5, 5)

print(g)