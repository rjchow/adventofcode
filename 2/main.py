import copy

def execute_program(noun, verb, program):
#   print("p0", program[0])
  program[1] = noun
  program[2] = verb
#   print(noun, verb)
#   print(program)
  not_halted = True
  instruction_counter = 0
  while not_halted:
    instruction_location = instruction_counter * 4
    instruction = program[instruction_location: instruction_location + 4]

    opcode = instruction[0]
    loc1 = instruction[1]
    loc2 = instruction[2]
    retr = instruction[3]

    # print(opcode)

    if opcode == 1:
      operand1 = program[loc1]
      operand2 = program[loc2]
      program[retr] = operand1 + operand2
      # print("add")
    if opcode == 2:
      operand1 = program[loc1]
      operand2 = program[loc2]
      program[retr] = operand1 * operand2
      # print("mult")

    if opcode == 99:
    #   print("exit")
      not_halted = False

    instruction_counter = instruction_counter + 1
  
  return program[0]


with open("./input.txt", "r") as f:
  for line in f:
    program = list(map(int, line.split(",")))

    # print(execute_program(12, 2, program))
    for noun in range(0, 100):
        for verb in range(0, 100):
            # print(noun, verb)
            try:
                retr = execute_program(noun, verb, copy.deepcopy(program))
                # print(program[0])
                # print(retr)
                if (retr == 19690720):
                    print(noun, verb)
                    print(100 * noun + verb)
            except:
                print("failed", noun, verb)
                pass
    # # print(retr)
