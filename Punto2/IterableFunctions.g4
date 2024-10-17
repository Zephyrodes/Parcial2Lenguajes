grammar IterableFunctions;

// Reglas Léxicas
NUMBER      : [0-9]+('.'[0-9]+)?;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;
WS          : [ \t\r\n]+ -> skip ;

// Reglas Sintácticas
program     : (statement)* EOF ;
statement   : mapFunction
            | filterFunction ;

mapFunction : 'MAP' '(' IDENTIFIER ',' iterable ')' ;
filterFunction : 'FILTER' '(' IDENTIFIER ',' iterable ')' ;
iterable    : list | tuple ;
list        : '[' expression (',' expression)* ']' ;
tuple       : '(' expression (',' expression)* ')' ;
expression  : NUMBER | IDENTIFIER ;

