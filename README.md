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
### II. Principles <a name="principles"></a>
### III. Grammar <a name="grammar"></a>
#### 1. Instruction set
| Command | Description       |
|---------|-------------------|
| \>      | Increment pointer |
| <       | Decrement pointer |
| +       | Increment byte at pointer |
| -       | Decrement byte at pointer |
| o       | Output byte at pointer |
| i       | Input byte and place it at pointer |
| ˇ       | Push byte at pointer to the top of the stack |
| ^       | Pop byte from the top of the stack and place it at pointer |
| ;       | Swap byte at pointer with the byte on the top of the stack |
| {       | Jump to matching } if byte at pointer is zero |
| }       | Jump to matching { if byte at pointer is non zero |
| :*text*: | Comment |

### IV. Examples <a name="examples"></a>
### V. Implementations <a name="implementations"></a>
### VI. Acknowledgement <a name="acknowledgement"></a>