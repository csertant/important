from collections import deque

MEMORY_SIZE = 30000
MAX_STACK_SIZE = 1000


def execute_operation_atomic(operation: str, ptr: int, memory: list, sptr: int, stack: deque) -> None:
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
    else:
        raise SyntaxError(1)


def output_byte_atomic(byte: int):
    print(byte)


def input_byte_atomic() -> int:
    return int(input())
