grammar Fourier;

// Reglas para expresiones matemáticas

prog: (funcionDecl | fourierTransform | tablaTransform)*;

expr: expr op=('*' | '/') expr       # mulDiv
    | expr op=('+' | '-') expr       # addSub
    | expr '^' expr                  # power
    | '-' expr                       # negate
    | '(' expr ')'                   # parens
    | 'pi'                           # piExpr
    | ID                             # idExpr
    | NUMBER                         # numberExpr
    | 'sin' '(' expr ')'             # sinExpr
    | 'cos' '(' expr ')'             # cosExpr
    | 'exp' '(' expr ')'             # expExpr
    ;

// Definición de funciones
funcionDecl: 'funcion' ID '(' ID ')' '=' expr;

// Transformada de Fourier
fourierTransform: 'transformada' 'de' ID '(' ID ')';

// Uso de la tabla de pares transformados
tablaTransform: 'tabla' '[' ID ']' '=' expr;

// Tokens
PI     : 'pi';
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+('.'[0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;
