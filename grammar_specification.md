# aeonius grammar specification

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN EOL code END

code: ε
    | assignment code

#TODO: where
assignment: pattern '=' exp EOL
	   | DEF IDENTIFIER ':' EOL INDENT multipatternmatch UNDENT
          | DEF IDENTIFIER ':' pattern match
          | OP '(' OPIDENTIFIER ')' ':' EOL INDENT multipatternmatch UNDENT
          | OP '(' OPIDENTIFIER ')' ':' pattern match

multipatternmatch: pattern match
                 | multipatternmatch pattern match

multicondmatch: exp match
               | multicondmatch '|' exp match
               | multicondmatch '|' match

match: RIGHTARROW INDENT exp EOL UNDENT
     | RIGHTARROW INDENT multipatternmatch UNDENT
     | RIGHTARROW EOL INDENT multipatternmatch UNDENT
     | '|' INDENT multicondmatch UNDENT


primitive: INTEGER
         | FLOAT
         | STRING
         | FALSE
         | TRUE
         | NONE


const: primitive
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
   | IDENTIFIER arguments		#function call
   | '(' exp ')'	              #Wrapped in brackets
   | LAMBDA IDENTIFIER ':' exp
   | exp IF exp ELSE exp
   | exp OPIDENTIFIER exp 		#Operator
   | exp FOR pattern IN exp
   | exp FOR pattern IN exp IF exp
   | '{' IDENTIFIER ':' exp FOR pattern IN exp '}'
   | '{' IDENTIFIER ':' exp FOR pattern IN exp IF exp '}'

tupleexp: exp ','
            | nonsingletupleexp
            | nonsingletupleexp ','

nonsingletupleexp: exp ',' exp
                     | nonsingletupleexp ',' exp

iterexp: nonemptyiterexp
       | nonemptyiterexp ','

nonemptyiterexp: exp
	       | nonemptyiterexp ',' exp

dictexp: nonemptydictexp
       | nonemptydictexp ','
	 
nonemptydictexp: exp ':' exp
	       | nonemptydictexp ',' exp ':' exp


arguments: exp
         | exp arguments



pattern: const
       | '_'
       | IDENTIFIER
#       | nonemptyiterpattern             #TODO
       | '(' pattern ')'
       | '(' tuplepattern ')'
       | '[' iterpattern ']'
       | '{' dictpattern '}'

tuplepattern: pattern ','
            | nonsingletuplepattern
            | nonsingletuplepattern ','

nonsingletuplepattern: pattern ',' pattern
                     | nonsingletuplepattern ',' pattern

iterpattern: nonemptyiterpattern
	    | nonemptyiterpattern ','

nonemptyiterpattern: pattern
		 | nonemptyiterpattern ',' pattern

dictpattern: nonemptydictpattern
	    | nonemptydictpattern ','

nonemptydictpattern: pattern ':' pattern
		 | nonemptydictpattern ',' pattern ':' pattern