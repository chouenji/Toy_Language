from my_token import *
class Tokenizer:
    def tokenize(self, s):
        tokens = []
        i = 0
        while i < len(s):
            i = self.extractToken(s, i, tokens)
            if i == -1:
                raise "error"

        tokens.append(Token('$', '$'))
        return tokens
   
    # extract one token starting at i, add the token to tokens, and return the index after the token.
    def extractToken(self, s, i, tokens):
        while i < len(s) and s[i] == ' ' or s[i] == '\t' or s[i] == '\n':
            i += 1
        if i == len(s):
            return i
        if s[i].isdigit():
            val = 0
            leading_zero = 0
            while True:
                if  val == 0:
                    if leading_zero == 0:
                        leading_zero += 1
                    else:
                        raise ValueError("Leading zero is not allowed!")
                
                val = val * 10 + ord(s[i]) - ord('0')
                i += 1    
                
                if i >= len(s) or not s[i].isdigit():
                    break
            
            
            tokens.append(Num(val).token)
            return i

        elif s[i].isalpha() or s[i] == "_":
            sb = ""
            while True:
                sb += s[i]
                i += 1
                if i >= len(s) or not s[i].isalpha() and not s[i].isdigit():
                    break
            
            tokens.append(Identifier(sb).token)
  
            return i

        elif self.isOperator(s[i]):
            tokens.append(Operator(s[i]).token)
            i += 1
            return i

        elif self.isParatherhesis(s[i]):
            tokens.append(Parenthesis(s[i]).token)
            i += 1
            return i
        
        elif s[i] == ';':
            tokens.append(Colon(s[i]).token)
            i+= 1
            return i
        else:
            return -1
        
       
    def isOperator(self, c):
        if c == '+' or c == '-' or c == '*' or c == '/' or c == '=':
            return True        
        return False
    
    def isParatherhesis(self, c):
        if c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}':
            return True
        return False

class Tag:
    ID = "ID"
    NUM = "NUM"
    OP = "OP"
    RPAR = "RPAR"
    LPAR = "LPAR"
    COLON = "COLON"

class Num:
    def __init__(self, v):
        self.value = str(v)
        self.tag = Tag.NUM
        self.token = Token(self.tag, self.value)

class Identifier:
    def __init__(self, s):
        self.lexeme = s
        self.tag = Tag.ID
        self.token = Token(self.tag, self.lexeme)
   

class Operator:
    def __init__(self, s):
        self.lexeme = s
        self.tag = Tag.OP
        self.token = Token(self.tag, self.lexeme)


class Operator():
    def __init__(self, s):
        self.lexeme = s
        self.tag = Tag.OP
        self.token = Token(self.tag, self.lexeme)


class Parenthesis:
    def __init__(self, s):
        self.lexeme = s
        if self.lexeme == '(':
            self.tag = Tag.RPAR
        else:
            self.tag = Tag.LPAR

        self.token = Token(self.tag, self.lexeme)

class Colon:
    def __init__(self, s):
        self.lexeme = s
        self.tag = Tag.COLON

        self.token = Token(self.tag, self.lexeme)