grammar Complejos;

/*
 * Reglas principales
 */

// La expresión principal puede ser una operación con números complejos o un número complejo solo.
expr: complex_expr EOF;

// Definición de una expresión compleja que incluye operaciones de suma, resta, multiplicación, y división.
complex_expr
    : complex_expr ('+' | '-') complex_term   # addSubExpr
    | complex_term                            # singleTermExpr
    ;

// Términos de una expresión compleja que incluyen multiplicación y división.
complex_term
    : complex_term ('*' | '/') complex_factor # mulDivExpr
    | complex_factor                          # singleFactorExpr
    ;

// Un factor puede ser un número complejo o estar entre paréntesis.
complex_factor
    : '(' complex_expr ')'                    # parenExpr
    | complex_number                          # complexNumExpr
    ;

// Definición de un número complejo, compuesto de una parte real, una parte imaginaria o ambas.
complex_number
    : REAL_SIGNED ( '+' | '-' ) IMAG_PART     # complexFull
    | REAL_SIGNED                             # realOnly
    | IMAG_PART                               # imagOnly
    ;

/*
 * Reglas para los tokens
 */

// Definimos el formato de los números reales y las partes imaginarias.
// Un número real puede ser positivo o negativo y puede tener una parte decimal.
REAL_SIGNED: [+-]? REAL ;
REAL: DIGIT+ ( '.' DIGIT+ )? ;

// La parte imaginaria es similar a un número real, pero seguida por 'i'.
IMAG_PART: [+-]? REAL 'i';

// Los dígitos son necesarios para definir números.
fragment DIGIT: [0-9] ;

/*
 * Espacios en blanco y comentarios
 */
WS: [ \t\r\n]+ -> skip ;
