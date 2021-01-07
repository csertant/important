from collections import deque

MEMORY_SIZE = 30000
MAX_STACK_SIZE = 1000


def execute_operation(pc: int, operation: str, ptr: int, memory: list, sptr: int, stack: deque, is_looping: bool,
                      loop_start: deque, loop_end: deque, inner_loops: int) -> (int, int, bool):
    if is_looping:
        if operation == '{':
            inner_loops += 1
        if operation == '}':
            if inner_loops == 0:
                is_looping = False
            else:
                inner_loops -= 1

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
    elif operation == '{':
        if memory[ptr] != 0:
            is_looping = True
            loop_start.append(pc)
        else:
            pc = loop_end.pop()
    elif operation == '}':
        if memory[ptr] != 0:
            pc = loop_start[-1]
        else:
            loop_start.pop()
    else:
        raise SyntaxError("Invalid operation: {}".format(operation))

    return pc, ptr, is_looping


def output_byte_atomic(byte: int):
    print(byte)


def input_byte_atomic() -> int:
    return int(input())
