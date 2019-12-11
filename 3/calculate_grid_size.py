def calculate_grid_size(program):
    length = 0
    width = 0

    directions = breakdown_directions(program)

    left = sum(directions["L"])
    right = sum(directions["R"])
    up = sum(directions["U"])
    down = sum(directions["D"])

    


    return (length, width)


def breakdown_directions(program):
    directions = {
        "L": [],
        "R": [],
        "U": [],
        "D": []
    }

    for vector in [token.strip() for token in program.split(",")]:
        direction = list(vector)[0]
        directions[direction].append(int(vector[1:]))


    return directions