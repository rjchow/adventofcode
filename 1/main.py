

f = open("./input.txt", "r")

def calc_fuel(module_mass):
    calc = (module_mass // 3) - 2
    return calc if calc > 0 else 0

def calc_fuel_recursive(module_mass):
    calc = calc_fuel(module_mass)
    return 0 if calc == 0 else calc + calc_fuel_recursive(calc)

total_fuel = 0
for line in f:
    total_fuel += calc_fuel_recursive(int(line))

print(total_fuel)

