C_HEADER = '/*\nThis source was automatically generated by The IMPORTANT Interpreter & Compiler.\n*/'
C_INCLUDE = '#include <stdio.h>\n#include <stdlib.h>\n#include "stack.c"\n'
C_MAIN = 'int main(int argc, char **argv) {\n\t\tchar tape[30000]={0};\n\t\tchar* ptr = tape;\n\t\tstruct Stack* ' \
         'stack = createStack(1000);\n'
C_END = '}'


def important_compile(code) -> str:
    code_list = [C_HEADER, C_INCLUDE, C_MAIN]

    for operation in code:
        if operation == '>':
            code_list.append('\t\t++ptr;')
        elif operation == '<':
            code_list.append('\t\t--ptr;')
        elif operation == '+':
            code_list.append('\t\t++*ptr;')
        elif operation == '-':
            code_list.append('\t\t--*ptr;')
        elif operation == '.':
            code_list.append('\t\tputchar(*ptr);')
        elif operation == ',':
            code_list.append('\t\t*ptr = getchar();')
        elif operation == '{':
            code_list.append('\twhile(*ptr) {')
        elif operation == '}':
            code_list.append('\t}')
        elif operation == 'ˇ':
            code_list.append("\t\tpush(stack, *ptr);")
        elif operation == '^':
            code_list.append('\t\t*ptr = pop(stack);')
        elif operation == ';':
            code_list.append('\t\tchar tmp = *ptr;\n\t\t*ptr = pop(stack);\n\t\tpush(stack, tmp);')
        else:
            raise SyntaxError("Invalid operation: {}".format(operation))

    code_list.append(C_END)

    return '\n'.join(code_list)
