from my_tokenizer import Tokenizer
import math

class Parser:
    def __init__(self, line):
        self.tokens = Tokenizer().tokenize(line)
        self.token_loop = iter(self.tokens)
        self.current_token = next(self.token_loop)
        self.variables = {}
        self.current_variable = ''
        self.previous_variable = ''
        self.interpreter()      
        self.output()

     
     # gets new token
    def next_token(self):
        if self.current_token.val == '$':
            return
        else:
            self.current_token = next(self.token_loop)
    
    # check if current token is equal to expected token
    def match(self, expected_token):
        if self.current_token.val != expected_token:
            print ('error')
            raise Exception('Syntax Error: ', self.current_token.type ,' not equal to ', expected_token)

    #interpreter initialization
    def interpreter(self):
        while True:
            self.assignment()
            if self.current_token.val == '$':
                return True

    def assignment(self):
        if self.current_token.type == 'ID':
            self.current_variable = self.current_token.val
            self.next_token()
            self.match('=')
            exp = self.exp()
            self.match(';')
            self.previous_variable = self.current_variable
            self.variables[self.current_variable] = exp
            return

        elif self.current_token.val == ';':
            self.next_token()
        else:
            self.current_token.val = '$'

    def exp(self):
        try:
            factor = self.factor()
            term = self.term(factor)

            if term != math.inf:
                return term
            
            term = self.term_prime(factor)

            if term != math.inf:
                return term
        except:
            raise SyntaxError()


    def term_prime(self, factor):
        return factor + self.term_prime_left()
    

    #eliminate left recursion
    def term_prime_left(self):
        if self.current_token.val == '$' or self.current_token.val == ';' or self.current_token == ')':
            return 0

        if self.current_token.val == '+':
            factor = self.factor()
            return self.term_left() + factor -1

        if self.current_token.val == '-':
            factor = self.factor()
            return self.term_left() - factor -1

        else:
            return math.inf


    def term(self, factor):   
        return factor * self.term_left()
        
    
    #eliminate left recursion
    def term_left(self):
        self.next_token()   
        if self.current_token.val == '$' or self.current_token.val == ';' or self.current_token == ')':
            return 1

        if self.current_token.val == '*':
            factor = self.factor()
            return self.term_left() * factor 

        if self.current_token.val == '/':
            factor = self.factor()
            return self.term_left() / factor 

        else:
            return math.inf
    

    def factor(self):
        self.next_token()
        if self.current_token.val == '(':
            exp = self.exp()
            self.match(')')
            return exp
        elif self.current_token.val == '-':
            return -1 * self.factor()
        elif self.current_token.val == '+':
            return self.factor()
        elif self.current_token.type == 'NUM':
            return int(self.current_token.val)
        elif self.current_token.type == 'ID':
            if self.current_token.val in self.variables:
                return self.variables.get(self.previous_variable)
            else:
                print('error')
                raise Exception('Uninitialized variable error: ' + self.previous_token.type)

    #Print out the variables
    def output(self):
        for eachitem in self.variables.items():
           print('%s = %d' % (eachitem[0],eachitem[1]))