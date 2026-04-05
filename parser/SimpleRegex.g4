grammar SimpleRegex;

// Parser rules
regex
    : union
    ;

union
    : union '|' concat
    | concat
    ;

concat
    : concat repeat
    | repeat
    ;

repeat
    : atom '*'
    | atom '+'
    | atom '?'
    | atom
    ;

atom
    : CHAR
    | '(' regex ')'
    | '(' ')'
    ;

// Lexer rules
CHAR
    : [a-zA-Z0-9]
    ;

WS
    : [ \t\n\r] -> skip
    ;
