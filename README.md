# important

It's extremely important to make your code understandable with plenty of comments

## IMPORTANT Language Specification
*version 1.0*\
**Table of Contents**\
[I. Preface](#preface)\
[II. Principles](#principles)\
[III. Grammar](#grammar)\
[IV. Examples](#examples)\
[V. Implementations](#implementations)\
[VI. Acknowledgement](#acknowledgement)

### I. Preface <a name="preface"></a>
In order to prevent the imminent destructive battle between the world of programmers and ordinary people, and
to bridge the gap in understanding between the two parties (from at least one side), we created
a programming language that encourages programmers to write code that is fully understandable to anyone.
We know that a mere tool alone would not be a solution to such a serious problem, so it is IMPORTANT to note that
the IMPORTANT language is much more of an attitude-forming purpose than a practical one.
Those who don’t like that look for other languages, but who does, it’s a hero.
### II. Principles <a name="principles"></a>
It's IMPORTANT to comment and explain each and every piece of code in *IMPORTANT*, because it's **IMPORTANT**.
See examples in [section *IV*](#implementations).
### III. Grammar <a name="grammar"></a>
#### 3. Brief description
The IMPORTANT language is a somewhat extended version of brainfuck. It contains a stack with three operations associated
with it in addition to standard bf operations. Out of the usual pop and push operations, the swap operation is also
part of the language.
Another IMPORTANT feature is that the IMPORTANT language supports comments, and they even play an extremely IMPORTANT role
while running programs. It's almost magic.
#### 2. Instruction set
| Command | Description       |
|---------|-------------------|
| \>      | Increment pointer |
| <       | Decrement pointer |
| +       | Increment byte at pointer |
| -       | Decrement byte at pointer |
| .       | Output byte at pointer |
| ,       | Input byte and place it at pointer |
| ˇ       | Push byte at pointer to the top of the stack |
| ^       | Pop byte from the top of the stack and place it at pointer |
| ;       | Swap byte at pointer with the byte on the top of the stack |
| {       | Jump to matching } if byte at pointer is zero |
| }       | Jump to matching { if byte at pointer is non zero |
| :*text*: | Comment |

### IV. Examples <a name="examples"></a>
Small piece of code doing nothing:
```
:This code does nothing
because the pointer is zero when the program reaches the { curly bracket
so the - operation does not decreases the pointer instead it goes to the
closing } bracket and the program quits:
{-}
```
Small piece of code that does something:
```
:This program - called cat - writes its input directly to its output
Lets explain it briefly
, inputs data
{ finish program when there is zero data at pointer
. print data
, input data
} repeat this while there is nonzero data at pointer:
,{.,}
```
Piece of code that's not doing anything, because it isn't explained:
```
:This code is provided as-is and magically prints 'Hello World!' to the console:
+{-->-{>>+>-----<<}<--<---}>-.>>>+.>>..+++{.>}<<<<.+++.------.<<-.>>>>+.
```
### V. Implementations <a name="implementations"></a>
So far, we have not encountered further implementations of the language. If you did, open a pull request.
### VI. Acknowledgement <a name="acknowledgement"></a>
Yet another empty space for now.