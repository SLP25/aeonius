# aeonius grammar specification

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN EOL code END

code: ε
    | code assignment

assignment: pattern '=' exp EOL
	   | DEF IDENTIFIER ':' EOL INDENT multipatternmatch UNDENT
          | DEF IDENTIFIER ':' pattern match
          | OP '(' OPIDENTIFIER ')' ':' EOL INDENT multipatternmatch UNDENT
          | OP '(' OPIDENTIFIER ')' ':' pattern match

multipatternmatch: assignment
                 | pattern match
                 | multipatternmatch pattern match
                 | multipatternmatch assignment 

multicondmatch: exp match
              | multicondmatch '|' exp match
              | multicondmatch '|' match

match: RIGHTARROW INDENT exp EOL UNDENT
     | RIGHTARROW INDENT multipatternmatch UNDENT
     | RIGHTARROW EOL INDENT multipatternmatch UNDENT
     | '|' INDENT multicondmatch UNDENT


const: INTEGER
     | FLOAT
     | STRING
     | FALSE
     | TRUE
     | NONE
     | '(' const ')'
     | '(' tupleconst ')'
     | '[' iterconst ']'
     | '{' dictconst '}'

tupleconst: ε
          | const ','
          | nonsingletupleconst
          | nonsingletupleconst ','

nonsingletupleconst: const ',' const
                   | nonsingletupleconst ',' const

iterconst: ε
	  | nonemptyiterconst
         | nonemptyiterconst ','
	
nonemptyiterconst: const
		   | nonemptyiterconst ',' const

dictconst: ε
	  | nonemptydictconst
         | nonemptydictconst ','
	 
nonemptydictconst: const ':' const
		   | nonemptydictconst ',' const ':' const



exp: IDENTIFIER
   | const
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
               | UNPACKDICT exp
	        | nonemptydictexp ',' exp ':' exp
               | nonemptydictexp ',' UNPACKDICT exp



pattern: const
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