grammar RegExp;


prog: stat* returnStat

;

stat: VAR '=' exp NEWLINE
;

returnStat: 'return' exp NEWLINE
;

exp:  '('')'               # emptyString
      | '(' exp ')'        # nestedEXP   
      | CHAIN              # chain
      | 'Any' '(' ')'      # any
      | 'ZeroOrMore' '('exp')' # zeroOrMore
      | 'OneOrMore' '('exp')'  # oneOrMore
      | 'Maybe' '('exp')'      # maybe
      | 'Or' '(' exp (','exp)* ')'   # or
      | 'And' '(' exp (','exp)* ')'   # and
      | 'Concat' '(' exp (','exp)* ')'   # concat
      | 'Contains' '(' exp  ')'   # contains
      | 'Tam' '(' INT ')'   # tam
      | 'TamMin' '(' INT ')'   # tamMin
      | 'TamMax' '(' INT ')'   # tamMax
      | 'Prefix' '(' exp ')'   # prefix
      | 'Suffix' '(' exp ')'   # suffix
      | VAR                    # varExp

;





INT: [0-9];
VAR: [A-Z]+[0-9]+;
CHAIN: [a-z0-9]+;
NEWLINE:'\r'? '\n' ; 
WS  :   [ \t]+ -> skip ;










