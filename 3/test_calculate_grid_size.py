from calculate_grid_size import calculate_grid_size, breakdown_directions

# def test_1():
#     assert(calculate_grid_size("R5") == (5, 0))

# def test_2():
#     assert(calculate_grid_size("R5, L6") == (1, 0))


def test_3():
    assert(breakdown_directions("R5") == {"R": [5], "L": [], "U": [], "D": []})
    assert(breakdown_directions("L5") == {"R": [], "L": [5], "U": [], "D": []})
    assert(breakdown_directions("D5") == {"R": [], "L": [], "U": [], "D": [5]})
    assert(breakdown_directions("U5") == {"R": [], "L": [], "U": [5], "D": []})
    assert(breakdown_directions("R1, L2, D3, U5") ==
           {"R": [1], "L": [2], "U": [5], "D": [3]})
    assert(breakdown_directions("R1, R3, R5") == {
           "R": [1, 3, 5], "L": [], "U": [], "D": []})
