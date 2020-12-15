/*---------------------------------------------------
Implementation of stack data structure in C.
Extension for compiling IMPORTANT code to C language.
v1.0
---------------------------------------------------*/
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 1000

// A structure to represent a stack
struct Stack {
    int top;
    unsigned capacity;
    char* array;
};

// Function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    if(capacity <= MAXSIZE) {
        stack->capacity = capacity;
    }
    else {
        stack->capacity = MAXSIZE;
    }
    stack->top = -1;
    stack->array = (char*)malloc(stack->capacity * sizeof(char));
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
    return stack->top == stack->capacity - 1;
}

// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}

// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, char item)
{
    if (isFull(stack))
        return;
    stack->array[++stack->top] = item;
    //printf("%d pushed to stack\n", item);
}

// Function to remove an item from stack.  It decreases top by 1
char pop(struct Stack* stack)
{
    if (isEmpty(stack))
        return '';
    return stack->array[stack->top--];
}

// Function to return the top from stack without removing it
char peek(struct Stack* stack)
{
    if (isEmpty(stack))
        return '';
    return stack->array[stack->top];
}