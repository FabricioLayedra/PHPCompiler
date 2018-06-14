import ply.lex as lex

delimeters = ('LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET')

tokens = delimeters + (
    "CHAR",
    "NUM",
    "OPEN_TAG",
    "CLOSE_TAG",
    "php",
    "ECHO",
    "VARIABLE",
    "LCURLYBRACKET",
    "RCURLYBRACKET",
    "EQUALS",
    "SEMICOLON",
    "QUOTE",
    "DOT",
    "CONDITIONAL",
    "ARITMETHIC_OP"
)



t_ignore         = " \t"
t_CHAR           = r"[a-z]"
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_RBRACKET       = r'\]'
t_LBRACKET       = r'\['
t_RCURLYBRACKET  = r'\}'
t_LCURLYBRACKET  = r'\{'
t_EQUALS         = r'='
t_SEMICOLON      = r';'
t_DOT            = r'\.'
t_ECHO           = r'echo'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_OPEN_TAG(t):
    r'<[?%]((php[ \t\r\n]?)|=)?'
    if '=' in t.value: t.type = 'OPEN_TAG_WITH_ECHO'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_CLOSE_TAG(t):
    r'[?%]>\r?\n?'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_VARIABLE(t):
    r'\$[A-Za-z_\x7f-\xff][\w_]*'
    return t

def t_QUOTE(t):
    r'"'

def t_CONDITIONAL(t):
	r'(el)?if|else(if)?|for(each)?|include(_once)?|require(_once)?|(do-)?while|return|continue|switch|declare|goto|break'
	return t

def t_ARITMETHIC_OP(t):
    r'\+|-|\*(\*)?|\/|%|\-'
    return t

def t_NUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    print (t.lexer.current_state)
    print (dir(t.lexer))
    raise TypeError("unknown char '%s'"%(t.value))

input_data = input("Ingrese código para verificar léxico en PHP (Ingrese SALIR para terminar): ")

while(input_data!="SALIR"):
    lex.lex()
    lex.input(input_data)
    for tok in iter(lex.token, None):
        print (repr(tok.type), repr(tok.value))
    input_data = input("Ingrese código para verificar léxico en PHP: ")



