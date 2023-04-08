# Aeonius grammar specification

```

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN code END

code: ε
    | COMMENT code
    | function code
    | lambda code

lambda: IDENTIFIER ASSIGN expression

function: DEF IDENTIFIER COLON patternmatch
operator: OP OPENROUNDPAR IDENTIFIER CLOSEROUNDPAR COLON patternmatch

comment: ε
       | COMMENT

patternmatch: match RIGHTARROW expression comment
            | match RIGHTARROW expression comment patternmatch

match: matchitem
     | matchitem RIGHTARROW match

matchitem: INTEGER
         | FLOAT
         | UNDERSCORE
         | STRING
         | IDENTIFIER
         | OPENROUNDPAR itermatch CLOSEROUNDPAR
         | OPENSQUAREBRAC itermatch CLOSESQUAREBRAC
         | OPENSQUAREBRAC CLOSESQUAREBRAC
         | dictmatch
         | itermatch


dictmatch: OPENCURLYBRAC CLOSECURLYBRAC
         | OPENCURLYBRAC dictmatchid COLON dictmatchid CLOSECURLYBRAC
         | OPENCURLYBRAC dictmatchid COLON dictmatchid COMMA KEYARGS dictmatchid CLOSECURLYBRAC

dictmatchid: IDENTIFIER
           | UNDERSCORE

itermatch: matchitem
         | KEYARGS IDENTIFIER
         | KEYARGS UNDERSCORE
         | matchitem COMMA itermatch

expression: IDENTIFIER
          | INTEGER
          | FLOAT
          | STRING
          | IDENTIFIER arguments
          | OPENROUNDPAR expression CLOSEROUNDPAR # Wrapped in brackets
          | patternmatch
          | expression PLUS expression
          | expression MINUS expression
          | expression TIMES expression
          | expression DIV expression
          | expression MOD expression
          | expression EQUALS expression
          | expression LESSTHANOREQUAL expression
          | expression LESSTHAN expression
          | expression GREATERTHANOREQUAL expression
          | expression GREATERTHAN expression
          | LAMBDA IDENTIFIER COLON expression
          | expression IF expression ELSE expression
          | expression IDENTIFIER expression #Operator
          | expression FOR IDENTIFIER IN IDENTIFIER
          | expression FOR IDENTIFIER IN INDENTIFIER IF expression
          | OPENCURLYBRAC IDENTIFIER COLON expression FOR IDENTIFIER IN IDENTIFIER CLOSECURLYBRAC
          | OPENCURLYBRAC IDENTIFIER COLON expression FOR IDENTIFIER IN IDENTIFIER IF expression CLOSECURLYBRAC
          | expressionlist
          | expressiontuple
          | expressiondict

expressionlist: OPENSQUAREBRAC CLOSESQUAREBRAC
              | OPENSQUAREBRAC multiexpression CLOSESQUAREBRAC

expressiontuple: OPENROUNDPAR multiexpression CLOSEROUNDPAR

expressiondict: OPENCURLYBRAC CLOSECURLYBRAC
              | OPENCURLYBRAC multidictexp CLOSECURLYBRAC

multidictexp: expression COLON expression
            | expression COLON expression multidictexp

multiexpression: expression
               | expression COMMA multiexpression


arguments: ε
         | expression arguments

patternmatch: matchitem PIPE expression RIGHTARROW expression
            | matchitem PIPE expression RIGHTARROW expression patternmatch
```