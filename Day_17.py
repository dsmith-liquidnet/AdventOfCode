A = 117440
B = 0
C = 0

program = [0,3,5,4,3,0]

def combo_operands(x):
    if 0 <= x <=3:
        return x
    if x==4:
        return A
    if x==5:
        return B
    if x==6:
        return C

pointer = 0

output = []

while pointer < len(program):
    instruction = program[pointer]
    if instruction == 0:
        A = A>>combo_operands(program[pointer+1])
    if instruction == 1:
        B = program[pointer+1] ^ B
    if instruction == 2:
        B = combo_operands(program[pointer+1])%8
    if instruction == 3:
        if A != 0:
            pointer = program[pointer+1]
            continue
    if instruction == 4:
        B = B ^ C
    if instruction == 5:
        output.append(combo_operands(program[pointer+1]) % 8)
    if instruction == 6:
        B = A>>combo_operands(program[pointer+1])
    if instruction == 7:
        C = A>>combo_operands(program[pointer+1])
    pointer += 2

print (output)