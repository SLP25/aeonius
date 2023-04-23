# Aeonius grammar specification

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN EOL code END

code: ε
    | assignment code

assignment: pattern '=' exp EOL
	   | DEF IDENTIFIER ':' patternmatch       #TODO: where
          | OP '(' OPIDENTIFIER ')' ':' patternmatch

#TODO: indentation
patternmatch: match EOL
            | match EOL patternmatch

match: pattern RIGHTARROW exp
     | pattern RIGHTARROW match


primitive: INTEGER
         | FLOAT
         | STRING


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



exp: IDENTIFIER
   | const
   | '(' tupleexp ')'
   | '[' iterexp ']'
   | '{' dictexp '}'
#   | IDENTIFIER arguments		#function call
   | '(' exp ')'	              #Wrapped in brackets
#   | match				#lambda
   | LAMBDA IDENTIFIER ':' exp	#lambda but with python syntax
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


#arguments: ε
#         | exp arguments
