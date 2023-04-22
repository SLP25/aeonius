# Aeonius grammar specification

grammar: ε
       | aeonius grammar
       | PYTHONCODE grammar

aeonius: BEGIN code END

code: ε
    | assignment code

assignment: IDENTIFIER '=' exp
	  | DEF IDENTIFIER ':' patternmatch
	  | OP '(' IDENTIFIER ')' ':' patternmatch

#TODO: allow indentation to do stuff
patternmatch: match
            | match patternmatch

match: pattern RIGHTARROW exp
     | pattern RIGHTARROW match



pattern: const
       | '_'
       | IDENTIFIER
       | iterpattern
       | '(' iterpattern ')'
       | '[' iterpattern ']'
       | '{' dictpattern '}'
       
iterpattern: ε
	 | nonemptyiterpattern
	
nonemptyiterpattern: pattern
		 | nonemptyiterpattern ',' pattern

dictpattern: ε
	 | nonemptydictpattern
	 
nonemptydictpattern: pattern ':' pattern
		 | nonemptydictpattern ',' pattern ':' pattern 



exp: IDENTIFIER
   | const
   | '(' iterexp ')'
   | '[' iterexp ']'
   | '{' dictexp '}'
   | IDENTIFIER arguments		#function call
   | '(' exp ')'	              #Wrapped in brackets
   | match				#lambda
   | LAMBDA IDENTIFIER ':' exp	#lambda but with python syntax
   | exp IF exp ELSE exp
   | exp IDENTIFIER exp 		#Operator
   | exp FOR IDENTIFIER IN IDENTIFIER
   | exp FOR IDENTIFIER IN IDENTIFIER IF exp
   | '{' IDENTIFIER ':' exp FOR IDENTIFIER IN IDENTIFIER '}'
   | '{' IDENTIFIER ':' exp FOR IDENTIFIER IN IDENTIFIER IF exp '}'


iterexp: ε
       | nonemptyiterexp

nonemptyiterexp: exp
	       | iterexp ',' exp

dictexp: ε
       | nonemptydictexp
	 
nonemptydictexp: exp ':' exp
	       | nonemptydictexp ',' exp ':' exp


arguments: ε
         | exp arguments



const: INTEGER
     | FLOAT
     | STRING
     | '(' iterconst ')'
     | '[' iterconst ']'
     | '{' dictconst '}'
	
iterconst: ε
	 | nonemptyiterconst
	
nonemptyiterconst: const
		 | nonemptyiterconst ',' const

dictconst: ε
	 | nonemptydictconst
	 
nonemptydictconst: const ':' const
		 | nonemptydictconst ',' const ':' const
