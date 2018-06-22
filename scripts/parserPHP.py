import ply.yacc as yacc
from PHPCompiler_1a import tokens
import ply.lex as lex



precedence = (
    ('left', 'ARITMETHIC_OP'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
)

def p_assign(p):
    '''
     expr : VARIABLE EQUALS expr
    '''


def p_exprArithmetic(p):
    '''expr : NUM ARITMETHIC_OP NUM
    '''
    if (p[2] == '+'):
        p[0] = p[1] + p[3]
    elif (p[2] == '-'):
        p[0] = p[1] - p[3]
    elif (p[2] == '/'):
        p[0] = p[1] / p[3]
    elif (p[2] == '*'):
        p[0] = p[1] * p[3]
    elif (p[2] == '%'):
        p[0] = p[1] % p[3]


def p_indexing(p):
    '''
     expr : ARRAY LBRACKET VARIABLE RBRACKET
    '''



parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)