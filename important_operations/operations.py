from collections import deque

MEMORY_SIZE = 30000
MAX_STACK_SIZE = 1000


def build_bracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == '{': temp_bracestack.append(position)
        if command == '}':
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


def execute(code: str) -> None:
    pc = 0
    ptr = 0
    memory = [0] * MEMORY_SIZE
    sptr = 1000
    stack = deque(maxlen=MAX_STACK_SIZE)
    bracemap = build_bracemap(code)

    while pc < len(code):
        operation = code[pc]
        if operation == '>':
            ptr = ptr + 1 if ptr < MEMORY_SIZE - 1 else 0
        elif operation == '<':
            ptr = ptr - 1 if ptr > 0 else MEMORY_SIZE - 1
        elif operation == '+':
            memory[ptr] += 1
        elif operation == '-':
            memory[ptr] -= 1
        elif operation == 'o':
            output_byte_atomic(memory[ptr])
        elif operation == 'i':
            memory[ptr] = input_byte_atomic()
        elif operation == 'ˇ':
            sptr -= 1
            stack.append(memory[ptr])
        elif operation == '^':
            sptr += 1
            memory[ptr] = stack.pop()
        elif operation == ';':
            if stack:
                memory[ptr], stack[-1] = stack[-1], memory[ptr]
        elif operation == '{' and memory[ptr] == 0:
            pc = bracemap[pc]
        elif operation == '}' and memory[ptr] != 0:
            pc = bracemap[pc]
        else:
            raise SyntaxError("Invalid operation: {}".format(operation))


def output_byte_atomic(byte: int):
    print(byte)


def input_byte_atomic() -> int:
    return int(input())
