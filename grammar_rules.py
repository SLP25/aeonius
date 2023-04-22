
def p_grammar1(v):
    "grammar : "
    v[0] = "ok"

def p_grammar2(v):
    "grammar : aeonius grammar"
    v[0] = "ok"

def p_grammar3(v):
    "grammar : PYTHONCODE grammar"
    v[0] = "ok"

def p_aeonius1(v):
    "aeonius : BEGIN code END"
    v[0] = "ok"

def p_code1(v):
    "code : "
    v[0] = "ok"

def p_code2(v):
    "code : assignment code"
    v[0] = "ok"

def p_assignment1(v):
    "assignment : IDENTIFIER '=' exp"
    v[0] = "ok"

def p_assignment2(v):
    "assignment : DEF IDENTIFIER ':' patternmatch"
    v[0] = "ok"

def p_assignment3(v):
    "assignment : OP '(' IDENTIFIER ')' ':' patternmatch"
    v[0] = "ok"

def p_patternmatch1(v):
    "patternmatch : match"
    v[0] = "ok"

def p_patternmatch2(v):
    "patternmatch : match patternmatch"
    v[0] = "ok"

def p_match1(v):
    "match : pattern RIGHTARROW exp"
    v[0] = "ok"

def p_match2(v):
    "match : pattern RIGHTARROW match"
    v[0] = "ok"

def p_pattern1(v):
    "pattern : const"
    v[0] = "ok"

def p_pattern2(v):
    "pattern : '_'"
    v[0] = "ok"

def p_pattern3(v):
    "pattern : IDENTIFIER"
    v[0] = "ok"

def p_pattern4(v):
    "pattern : iterpattern"
    v[0] = "ok"

def p_pattern5(v):
    "pattern : '(' iterpattern ')'"
    v[0] = "ok"

def p_pattern6(v):
    "pattern : '[' iterpattern ']'"
    v[0] = "ok"

def p_pattern7(v):
    "pattern : '{' dictpattern '}'"
    v[0] = "ok"

def p_iterpattern1(v):
    "iterpattern : "
    v[0] = "ok"

def p_iterpattern2(v):
    "iterpattern : nonemptyiterpattern"
    v[0] = "ok"

def p_nonemptyiterpattern1(v):
    "nonemptyiterpattern : pattern"
    v[0] = "ok"

def p_nonemptyiterpattern2(v):
    "nonemptyiterpattern : nonemptyiterpattern ',' pattern"
    v[0] = "ok"

def p_dictpattern1(v):
    "dictpattern : "
    v[0] = "ok"

def p_dictpattern2(v):
    "dictpattern : nonemptydictpattern"
    v[0] = "ok"

def p_nonemptydictpattern1(v):
    "nonemptydictpattern : pattern ':' pattern"
    v[0] = "ok"

def p_nonemptydictpattern2(v):
    "nonemptydictpattern : nonemptydictpattern ',' pattern ':' pattern "
    v[0] = "ok"

def p_exp1(v):
    "exp : IDENTIFIER"
    v[0] = "ok"

def p_exp2(v):
    "exp : const"
    v[0] = "ok"

def p_exp3(v):
    "exp : '(' iterexp ')'"
    v[0] = "ok"

def p_exp4(v):
    "exp : '[' iterexp ']'"
    v[0] = "ok"

def p_exp5(v):
    "exp : '{' dictexp '}'"
    v[0] = "ok"

def p_exp6(v):
    "exp : IDENTIFIER arguments		"
    v[0] = "ok"

def p_exp7(v):
    "exp : '(' exp ')'	              "
    v[0] = "ok"

def p_exp8(v):
    "exp : match				"
    v[0] = "ok"

def p_exp9(v):
    "exp : LAMBDA IDENTIFIER ':' exp	"
    v[0] = "ok"

def p_exp10(v):
    "exp : exp IF exp ELSE exp"
    v[0] = "ok"

def p_exp11(v):
    "exp : exp IDENTIFIER exp 		"
    v[0] = "ok"

def p_exp12(v):
    "exp : exp FOR IDENTIFIER IN IDENTIFIER"
    v[0] = "ok"

def p_exp13(v):
    "exp : exp FOR IDENTIFIER IN IDENTIFIER IF exp"
    v[0] = "ok"

def p_exp14(v):
    "exp : '{' IDENTIFIER ':' exp FOR IDENTIFIER IN IDENTIFIER '}'"
    v[0] = "ok"

def p_exp15(v):
    "exp : '{' IDENTIFIER ':' exp FOR IDENTIFIER IN IDENTIFIER IF exp '}'"
    v[0] = "ok"

def p_iterexp1(v):
    "iterexp : "
    v[0] = "ok"

def p_iterexp2(v):
    "iterexp : nonemptyiterexp"
    v[0] = "ok"

def p_nonemptyiterexp1(v):
    "nonemptyiterexp : exp"
    v[0] = "ok"

def p_nonemptyiterexp2(v):
    "nonemptyiterexp : iterexp ',' exp"
    v[0] = "ok"

def p_dictexp1(v):
    "dictexp : "
    v[0] = "ok"

def p_dictexp2(v):
    "dictexp : nonemptydictexp"
    v[0] = "ok"

def p_nonemptydictexp1(v):
    "nonemptydictexp : exp ':' exp"
    v[0] = "ok"

def p_nonemptydictexp2(v):
    "nonemptydictexp : nonemptydictexp ',' exp ':' exp"
    v[0] = "ok"

def p_arguments1(v):
    "arguments : "
    v[0] = "ok"

def p_arguments2(v):
    "arguments : exp arguments"
    v[0] = "ok"

def p_const1(v):
    "const : INTEGER"
    v[0] = "ok"

def p_const2(v):
    "const : FLOAT"
    v[0] = "ok"

def p_const3(v):
    "const : STRING"
    v[0] = "ok"

def p_const4(v):
    "const : '(' iterconst ')'"
    v[0] = "ok"

def p_const5(v):
    "const : '[' iterconst ']'"
    v[0] = "ok"

def p_const6(v):
    "const : '{' dictconst '}'"
    v[0] = "ok"

def p_iterconst1(v):
    "iterconst : "
    v[0] = "ok"

def p_iterconst2(v):
    "iterconst : nonemptyiterconst"
    v[0] = "ok"

def p_nonemptyiterconst1(v):
    "nonemptyiterconst : const"
    v[0] = "ok"

def p_nonemptyiterconst2(v):
    "nonemptyiterconst : nonemptyiterconst ',' const"
    v[0] = "ok"

def p_dictconst1(v):
    "dictconst : "
    v[0] = "ok"

def p_dictconst2(v):
    "dictconst : nonemptydictconst"
    v[0] = "ok"

def p_nonemptydictconst1(v):
    "nonemptydictconst : const ':' const"
    v[0] = "ok"

def p_nonemptydictconst2(v):
    "nonemptydictconst : nonemptydictconst ',' const ':' const"
    v[0] = "ok"
