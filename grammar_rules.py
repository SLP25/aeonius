
def p_grammar_1(v):
    "grammar : "
    v[0] = "ok"

def p_grammar_2(v):
    "grammar : aeonius grammar"
    v[0] = "ok"

def p_grammar_3(v):
    "grammar : PYTHONCODE grammar"
    v[0] = "ok"

def p_aeonius_1(v):
    "aeonius : BEGIN EOL code END"
    v[0] = "ok"

def p_code_1(v):
    "code : "
    v[0] = "ok"

def p_code_2(v):
    "code : assignment code"
    v[0] = "ok"

def p_assignment_1(v):
    "assignment : pattern '=' exp EOL"
    v[0] = "ok"

def p_assignment_2(v):
    "assignment : DEF IDENTIFIER ':' patternmatch       "
    v[0] = "ok"

def p_assignment_3(v):
    "assignment : OP '(' OPIDENTIFIER ')' ':' patternmatch"
    v[0] = "ok"

def p_patternmatch_1(v):
    "patternmatch : match EOL"
    v[0] = "ok"

def p_patternmatch_2(v):
    "patternmatch : match EOL patternmatch"
    v[0] = "ok"

def p_match_1(v):
    "match : pattern RIGHTARROW exp"
    v[0] = "ok"

def p_match_2(v):
    "match : pattern RIGHTARROW match"
    v[0] = "ok"

def p_primitive_1(v):
    "primitive : INTEGER"
    v[0] = "ok"

def p_primitive_2(v):
    "primitive : FLOAT"
    v[0] = "ok"

def p_primitive_3(v):
    "primitive : STRING"
    v[0] = "ok"

def p_const_1(v):
    "const : primitive"
    v[0] = "ok"

def p_const_2(v):
    "const : '(' const ')'"
    v[0] = "ok"

def p_const_3(v):
    "const : '(' tupleconst ')'"
    v[0] = "ok"

def p_const_4(v):
    "const : '[' iterconst ']'"
    v[0] = "ok"

def p_const_5(v):
    "const : '{' dictconst '}'"
    v[0] = "ok"

def p_tupleconst_1(v):
    "tupleconst : "
    v[0] = "ok"

def p_tupleconst_2(v):
    "tupleconst : const ','"
    v[0] = "ok"

def p_tupleconst_3(v):
    "tupleconst : nonsingletupleconst"
    v[0] = "ok"

def p_tupleconst_4(v):
    "tupleconst : nonsingletupleconst ','"
    v[0] = "ok"

def p_nonsingletupleconst_1(v):
    "nonsingletupleconst : const ',' const"
    v[0] = "ok"

def p_nonsingletupleconst_2(v):
    "nonsingletupleconst : nonsingletupleconst ',' const"
    v[0] = "ok"

def p_iterconst_1(v):
    "iterconst : "
    v[0] = "ok"

def p_iterconst_2(v):
    "iterconst : nonemptyiterconst"
    v[0] = "ok"

def p_iterconst_3(v):
    "iterconst : nonemptyiterconst ','"
    v[0] = "ok"

def p_nonemptyiterconst_1(v):
    "nonemptyiterconst : const"
    v[0] = "ok"

def p_nonemptyiterconst_2(v):
    "nonemptyiterconst : nonemptyiterconst ',' const"
    v[0] = "ok"

def p_dictconst_1(v):
    "dictconst : "
    v[0] = "ok"

def p_dictconst_2(v):
    "dictconst : nonemptydictconst"
    v[0] = "ok"

def p_dictconst_3(v):
    "dictconst : nonemptydictconst ','"
    v[0] = "ok"

def p_nonemptydictconst_1(v):
    "nonemptydictconst : const ':' const"
    v[0] = "ok"

def p_nonemptydictconst_2(v):
    "nonemptydictconst : nonemptydictconst ',' const ':' const"
    v[0] = "ok"

def p_pattern_1(v):
    "pattern : const"
    v[0] = "ok"

def p_pattern_2(v):
    "pattern : '_'"
    v[0] = "ok"

def p_pattern_3(v):
    "pattern : IDENTIFIER"
    v[0] = "ok"

def p_pattern_4(v):
    "pattern : '(' pattern ')'"
    v[0] = "ok"

def p_pattern_5(v):
    "pattern : '(' tuplepattern ')'"
    v[0] = "ok"

def p_pattern_6(v):
    "pattern : '[' iterpattern ']'"
    v[0] = "ok"

def p_pattern_7(v):
    "pattern : '{' dictpattern '}'"
    v[0] = "ok"

def p_tuplepattern_1(v):
    "tuplepattern : pattern ','"
    v[0] = "ok"

def p_tuplepattern_2(v):
    "tuplepattern : nonsingletuplepattern"
    v[0] = "ok"

def p_tuplepattern_3(v):
    "tuplepattern : nonsingletuplepattern ','"
    v[0] = "ok"

def p_nonsingletuplepattern_1(v):
    "nonsingletuplepattern : pattern ',' pattern"
    v[0] = "ok"

def p_nonsingletuplepattern_2(v):
    "nonsingletuplepattern : nonsingletuplepattern ',' pattern"
    v[0] = "ok"

def p_iterpattern_1(v):
    "iterpattern : nonemptyiterpattern"
    v[0] = "ok"

def p_iterpattern_2(v):
    "iterpattern : nonemptyiterpattern ','"
    v[0] = "ok"

def p_nonemptyiterpattern_1(v):
    "nonemptyiterpattern : pattern"
    v[0] = "ok"

def p_nonemptyiterpattern_2(v):
    "nonemptyiterpattern : nonemptyiterpattern ',' pattern"
    v[0] = "ok"

def p_dictpattern_1(v):
    "dictpattern : nonemptydictpattern"
    v[0] = "ok"

def p_dictpattern_2(v):
    "dictpattern : nonemptydictpattern ','"
    v[0] = "ok"

def p_nonemptydictpattern_1(v):
    "nonemptydictpattern : pattern ':' pattern"
    v[0] = "ok"

def p_nonemptydictpattern_2(v):
    "nonemptydictpattern : nonemptydictpattern ',' pattern ':' pattern "
    v[0] = "ok"

def p_exp_1(v):
    "exp : IDENTIFIER"
    v[0] = "ok"

def p_exp_2(v):
    "exp : const"
    v[0] = "ok"

def p_exp_3(v):
    "exp : '(' tupleexp ')'"
    v[0] = "ok"

def p_exp_4(v):
    "exp : '[' iterexp ']'"
    v[0] = "ok"

def p_exp_5(v):
    "exp : '{' dictexp '}'"
    v[0] = "ok"

def p_exp_6(v):
    "exp : '(' exp ')'	              "
    v[0] = "ok"

def p_exp_7(v):
    "exp : LAMBDA IDENTIFIER ':' exp	"
    v[0] = "ok"

def p_exp_8(v):
    "exp : exp IF exp ELSE exp"
    v[0] = "ok"

def p_exp_9(v):
    "exp : exp OPIDENTIFIER exp 		"
    v[0] = "ok"

def p_exp_10(v):
    "exp : exp FOR pattern IN exp"
    v[0] = "ok"

def p_exp_11(v):
    "exp : exp FOR pattern IN exp IF exp"
    v[0] = "ok"

def p_exp_12(v):
    "exp : '{' IDENTIFIER ':' exp FOR pattern IN exp '}'"
    v[0] = "ok"

def p_exp_13(v):
    "exp : '{' IDENTIFIER ':' exp FOR pattern IN exp IF exp '}'"
    v[0] = "ok"

def p_tupleexp_1(v):
    "tupleexp : exp ','"
    v[0] = "ok"

def p_tupleexp_2(v):
    "tupleexp : nonsingletupleexp"
    v[0] = "ok"

def p_tupleexp_3(v):
    "tupleexp : nonsingletupleexp ','"
    v[0] = "ok"

def p_nonsingletupleexp_1(v):
    "nonsingletupleexp : exp ',' exp"
    v[0] = "ok"

def p_nonsingletupleexp_2(v):
    "nonsingletupleexp : nonsingletupleexp ',' exp"
    v[0] = "ok"

def p_iterexp_1(v):
    "iterexp : nonemptyiterexp"
    v[0] = "ok"

def p_iterexp_2(v):
    "iterexp : nonemptyiterexp ','"
    v[0] = "ok"

def p_nonemptyiterexp_1(v):
    "nonemptyiterexp : exp"
    v[0] = "ok"

def p_nonemptyiterexp_2(v):
    "nonemptyiterexp : nonemptyiterexp ',' exp"
    v[0] = "ok"

def p_dictexp_1(v):
    "dictexp : nonemptydictexp"
    v[0] = "ok"

def p_dictexp_2(v):
    "dictexp : nonemptydictexp ','"
    v[0] = "ok"

def p_nonemptydictexp_1(v):
    "nonemptydictexp : exp ':' exp"
    v[0] = "ok"

def p_nonemptydictexp_2(v):
    "nonemptydictexp : nonemptydictexp ',' exp ':' exp"
    v[0] = "ok"
