from my_parser import Parser

#Comment out for testing inputs e.g x = 1 + 5; y = x * 30; z = y/2;
#syntax = Parser(input("Write a syntax:"))

# Test cases
# Parser("x=001;") // Error
# Parser("x2=0;") // Valid
# Parser("x=0 y=x; z=---(x+y);") // Error
# Parser("x=1;y=2;z=x+-y;") // Valid
#Parser("x=1+5; y=x*30; z=y/2;") // Valid
#Parser("x=500/2-50;") // Valid
