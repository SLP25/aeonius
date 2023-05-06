# aeonius grammar specification

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN EOL code END

code: ε
    | assignment code

assignment: pattern '=' exp EOL
	   | DEF IDENTIFIER ':' EOL INDENT defbody UNDENT
          | DEF IDENTIFIER ':' pattern match
          | OP '(' OPIDENTIFIER ')' ':' EOL INDENT defbody UNDENT
          | OP '(' OPIDENTIFIER ')' ':' pattern match

defbody: multipatternmatch code

multipatternmatch: pattern match
                 | multipatternmatch pattern match

multicondmatch: exp match
              | multicondmatch '|' exp match
              | multicondmatch '|' match

match: RESULTARROW INDENT exp EOL code UNDENT
     | RESULTARROW EOL INDENT exp EOL code UNDENT
     | RIGHTARROW INDENT defbody UNDENT
     | RIGHTARROW EOL INDENT defbody UNDENT
     | '|' INDENT multicondmatch UNDENT


primitive: INTEGER
         | FLOAT
         | STRING
         | FALSE
         | TRUE
         | NONE
         | '[' ']'
         | '{' '}'


exp: IDENTIFIER
   | primitive %prec PRIMITIVE
   | '(' tupleexp ')'
   | '[' iterexp ']'
   | '{' dictexp '}'
   | exp arguments %prec FUNC         	#function call
   | '(' exp ')'	                     #Wrapped in brackets
   | LAMBDA IDENTIFIER ':' exp
   | exp IF exp ELSE exp
   | exp operator exp %prec OPIDENTIFIER 	#Operator call
#   | operator exp		              #unary operator call
   | '(' operator ')'                     #operator function
   | exp FOR pattern IN exp
   | exp FOR pattern IN exp IF exp
   | '{' IDENTIFIER ':' exp FOR pattern IN exp '}'
   | '{' IDENTIFIER ':' exp FOR pattern IN exp IF exp '}'

arguments: exp %prec FUNC
         | arguments exp %prec FUNC

operator: OPIDENTIFIER
        | UNPACKITER
        | UNPACKDICT
        | '|'


elemexp: exp
       | UNPACKITER exp

tupleexp: elemexp ','
        | nonsingletupleexp
        | nonsingletupleexp ','

nonsingletupleexp: elemexp ',' elemexp
                 | nonsingletupleexp ',' elemexp

iterexp: nonemptyiterexp
       | nonemptyiterexp ','

nonemptyiterexp: elemexp
	        | nonemptyiterexp ',' elemexp

dictexp: nonemptydictexp
       | nonemptydictexp ','
	 
nonemptydictexp: exp ':' exp
	        | nonemptydictexp ',' exp ':' exp
               | nonemptydictexp ',' UNPACKDICT exp



pattern: primitive %prec PRIMITIVE
       | '_'
       | IDENTIFIER
#       | nonemptyiterpattern             #TODO
       | '(' pattern ')'
       | '(' tuplepattern ')'
       | '[' iterpattern ']'
       | '{' dictpattern '}'

tuplepattern: pattern ','
            | pattern ',' UNPACKITER pattern
            | nonsingletuplepattern
            | nonsingletuplepattern ','
            | nonsingletuplepattern ',' UNPACKITER pattern

nonsingletuplepattern: pattern ',' pattern
                     | nonsingletuplepattern ',' pattern

iterpattern: nonemptyiterpattern
	    | nonemptyiterpattern ','
           | nonemptyiterpattern ',' UNPACKITER pattern

nonemptyiterpattern: pattern
		     | nonemptyiterpattern ',' pattern

dictpattern: nonemptydictpattern
	    | nonemptydictpattern ','

nonemptydictpattern: pattern ':' pattern
		     | nonemptydictpattern ',' pattern ':' pattern
                   | nonemptydictpattern ',' UNPACKDICT pattern