import ply.yacc as yacc
import PHPCompiler.scripts.PHPCompiler_1a as lexer

listaTokens = lexer.tokens

precedence = (
    ('left', 'PLUS','MINUS', 'CONCAT', 'DIVIDE'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
)

def p_assign(p):
    '''
     expr : var EQUALS expr

    '''


def p_exprArithmetic(p):
    '''expr : expr ARITMETHIC_OP term
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


