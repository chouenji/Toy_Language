# Interpreter
Interpreter in Python V3 (Make sure your Python version is V3)

## Status
The tokenizer and parser have been implemented and example programs are interpreted. See tests directory for sample programs.

## Usage
Comment out the tests cases or input on main.py file.

## Description
This is an interpreter written in Python for [this simple language](http://www.sci.brooklyn.cuny.edu/~zhou/teaching/cis7120/project.html) (grammar described below), in which a program consists of assignments and each variable is assumed to be of the integer type. Only operators that give integer values are included. 

The interpreter can detect syntax errors, report uninitialized variables and perform the assignments (if there are no errors) and print the values of the variables after all assignments.

## Grammar
```
Program:
	Assignment*

Assignment:
	Identifier = Exp;

Exp: 
	Exp + Term | Exp - Term | Term

Term:
	Term * Fact  | Fact

Fact:
	( Exp ) | - Fact | + Fact | Literal | Identifier

Identifier:
     	Letter [Letter | Digit]*

Letter:
	a|...|z|A|...|Z|_

Literal:
	0 | NonZeroDigit Digit*
		
NonZeroDigit:
	1|...|9

Digit:
	0|1|...|9
```

## Test cases
Sample inputs and outputs. See the tests directory for more inputs.
```
Input 1
x = 001;
Output 1
error

Input 2
x_2 = 0;

Output 2
x_2 = 0

Input 3
x = 0
y = x;
z = ---(x+y);

Output 3
error

Input 4
x = 1;
y = 2;
z = ---(x+y)*(x+-y);

Output 4
x = 1
y = 2
z = 3

```
