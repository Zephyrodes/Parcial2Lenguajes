grammar MapFunction;

program
    : 'MAP' '(' function ',' iterable ')' EOF
    ;

function
    : 'lambda' '(' param (',' param)* ')' ':' expression
    ;

iterable
    : item_list
    | variable
    ;

item_list
    : '[' expression (',' expression)* ']'
    ;

variable
    : ID
    ;

expression
    : ID
    | NUMBER
    | '(' expression ')'
    | expression operator expression
    ;

param
    : ID
    ;

operator
    : '+'
    | '-'
    | '*'
    | '/'
    ;

ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
