from language import *

def p_grammar_1(v):
    "grammar : "
    v[0] = Grammar([])

def p_grammar_2(v):
    "grammar : aeonius grammar"
    v[0] = Grammar([v[1]] + v[2].snippets)

def p_grammar_3(v):
    "grammar : PYTHONCODE grammar"
    v[0] = Grammar([Python(v[1])] + v[2].snippets)

def p_aeonius_1(v):
    "aeonius : BEGIN EOL code END"
    v[0] = aeonius(v[3])

def p_code_1(v):
    "code : "
    v[0] = Code([])

def p_code_2(v):
    "code : assignment code"
    v[0] =  Code([v[1]] + v[2].assignments)

def p_assignment_1(v):
    "assignment : pattern '=' exp EOL"
    v[0] = AssignmentPattern(v[1], v[3])

def p_assignment_2(v):
    "assignment : DEF IDENTIFIER ':' EOL INDENT multipatternmatch UNDENT"
    v[0] = "ok"

def p_assignment_3(v):
    "assignment : DEF IDENTIFIER ':' pattern match"
    v[0] = "ok"

def p_assignment_4(v):
    "assignment : OP '(' OPIDENTIFIER ')' ':' EOL INDENT multipatternmatch UNDENT"
    v[0] = "ok"

def p_assignment_5(v):
    "assignment : OP '(' OPIDENTIFIER ')' ':' pattern match"
    v[0] = "ok"

def p_multipatternmatch_1(v):
    "multipatternmatch : pattern match"
    v[0] = "ok"

def p_multipatternmatch_2(v):
    "multipatternmatch : multipatternmatch pattern match"
    v[0] = "ok"

def p_multicondmatch_1(v):
    "multicondmatch : exp match"
    v[0] = "ok"

def p_multicondmatch_2(v):
    "multicondmatch : multicondmatch '|' exp match"
    v[0] = "ok"

def p_multicondmatch_3(v):
    "multicondmatch : multicondmatch '|' match"
    v[0] = "ok"

def p_match_1(v):
    "match : RIGHTARROW INDENT exp EOL UNDENT"
    v[0] = "ok"

def p_match_2(v):
    "match : RIGHTARROW INDENT multipatternmatch UNDENT"
    v[0] = "ok"

def p_match_3(v):
    "match : RIGHTARROW EOL INDENT multipatternmatch UNDENT"
    v[0] = "ok"

def p_match_4(v):
    "match : '|' INDENT multicondmatch UNDENT"
    v[0] = "ok"

def p_primitive_1(v):
    "primitive : INTEGER"
    v[0] = v[1]

def p_primitive_2(v):
    "primitive : FLOAT"
    v[0] = v[1]

def p_primitive_3(v):
    "primitive : STRING"
    v[0] = v[1]

def p_primitive_4(v):
    "primitive : FALSE"
    v[0] = False

def p_primitive_5(v):
    "primitive : TRUE"
    v[0] = True

def p_primitive_6(v):
    "primitive : NONE"
    v[0] = None

def p_const_1(v):
    "const : primitive"
    v[0] = PrimitiveConstant(v[1])

def p_const_2(v):
    "const : '(' const ')'"
    v[0] = BracketConstant(v[2])

def p_const_3(v):
    "const : '(' tupleconst ')'"
    v[0] = TupleConstant(v[2])

def p_const_4(v):
    "const : '[' iterconst ']'"
    v[0] = ListConstant(v[2])

def p_const_5(v):
    "const : '{' dictconst '}'"
    v[0] = DictConstant(v[2])

def p_tupleconst_1(v):
    "tupleconst : "
    v[0] = EmptyTupleConstantContent()

def p_tupleconst_2(v):
    "tupleconst : const ','"
    v[0] = NonEmptyTupleConstantContent(v[1], True)

def p_tupleconst_3(v):
    "tupleconst : nonsingletupleconst"
    v[0] = NonEmptyTupleConstantContent(v[1].constants, False)

def p_tupleconst_4(v):
    "tupleconst : nonsingletupleconst ','"
    v[0] = NonEmptyTupleConstantContent(v[1].constants, True)

def p_nonsingletupleconst_1(v):
    "nonsingletupleconst : const ',' const"
    v[0] = NonEmptyTupleConstantContent([v[1], v[3]], False)

def p_nonsingletupleconst_2(v):
    "nonsingletupleconst : nonsingletupleconst ',' const"
    v[0] = NonEmptyTupleConstantContent(v[1].constants + [v[3]], False)

def p_iterconst_1(v):
    "iterconst : "
    v[0] = EmptyListConstantContent()

def p_iterconst_2(v):
    "iterconst : nonemptyiterconst"
    v[0] = NonEmptyListConstantContent(v[1].constants, False)

def p_iterconst_3(v):
    "iterconst : nonemptyiterconst ','"
    v[0] = NonEmptyListConstantContent(v[1].constants, True)

def p_nonemptyiterconst_1(v):
    "nonemptyiterconst : const"
    v[0] = NonEmptyListConstantContent([v[1]], False)

def p_nonemptyiterconst_2(v):
    "nonemptyiterconst : nonemptyiterconst ',' const"
    v[0] = NonEmptyListConstantContent(v[1].constants + [v[3]], False)

def p_dictconst_1(v):
    "dictconst : "
    v[0] = EmptyDictConstantContent()

def p_dictconst_2(v):
    "dictconst : nonemptydictconst"
    v[0] = NonEmptyDictConstantContent(v[1], False)

def p_dictconst_3(v):
    "dictconst : nonemptydictconst ','"
    v[0] = NonEmptyDictConstantContent(v[1], True)

def p_nonemptydictconst_1(v):
    "nonemptydictconst : const ':' const"
    v[0] = NonEmptyDictConstantContent([(v[1], v[3])], False)

def p_nonemptydictconst_2(v):
    "nonemptydictconst : nonemptydictconst ',' const ':' const"
    v[0] =  NonEmptyDictConstantContent(v[1] + [(v[3], v[5])], False)

def p_exp_1(v):
    "exp : IDENTIFIER"
    v[0] = IdentifierExpression(v[1])

def p_exp_2(v):
    "exp : const"
    v[0] = ConstantExpression(v[1])

def p_exp_3(v):
    "exp : '(' tupleexp ')'"
    v[0] = TupleExpression(v[2])

def p_exp_4(v):
    "exp : '[' iterexp ']'"
    v[0] = ListExpression(v[2])

def p_exp_5(v):
    "exp : '{' dictexp '}'"
    v[0] = DictExpression(v[2])

def p_exp_6(v):
    "exp : IDENTIFIER arguments		"
    v[0] = "ok"

def p_exp_7(v):
    "exp : '(' exp ')'	              "
    v[0] = BracketExpression(v[2])

def p_exp_8(v):
    "exp : LAMBDA IDENTIFIER ':' exp"
    v[0] = LambdaExpression(v[2], v[4])

def p_exp_9(v):
    "exp : exp IF exp ELSE exp"
    v[0] = IfElseExpression(v[3], v[1], v[5])

def p_exp_10(v):
    "exp : exp OPIDENTIFIER exp 		"
    v[0] = OperationExpression(v[2], v[1], v[3])

def p_exp_11(v):
    "exp : exp FOR pattern IN exp"
    v[0] = ForLoopExpression(v[1], v[3], v[5])

def p_exp_12(v):
    "exp : exp FOR pattern IN exp IF exp"
    v[0] = ForLoopExpression(v[1], v[3], v[5], v[7])

def p_exp_13(v):
    "exp : '{' IDENTIFIER ':' exp FOR pattern IN exp '}'"
    v[0] = DictionaryCompreensionExpression(v[2], v[4], v[6], v[8])

def p_exp_14(v):
    "exp : '{' IDENTIFIER ':' exp FOR pattern IN exp IF exp '}'"
    v[0] = DictionaryCompreensionExpression(v[2], v[4], v[6], v[8], v[10])

def p_tupleexp_1(v):
    "tupleexp : exp ','"
    v[0] = NonEmptyTupleExpressionContent(v[1], True)

def p_tupleexp_2(v):
    "tupleexp : nonsingletupleexp"
    v[0] = NonEmptyTupleExpressionContent(v[1].expressions, False)

def p_tupleexp_3(v):
    "tupleexp : nonsingletupleexp ','"
    v[0] = NonEmptyTupleExpressionContent(v[1].expressions, True)

def p_nonsingletupleexp_1(v):
    "nonsingletupleexp : exp ',' exp"
    v[0] = NonEmptyTupleExpressionContent([v[1],v[3]], False)

def p_nonsingletupleexp_2(v):
    "nonsingletupleexp : nonsingletupleexp ',' exp"
    v[0] = NonEmptyTupleExpressionContent(v[1].expressions + [v[3]], False)

def p_iterexp_1(v):
    "iterexp : nonemptyiterexp"
    v[0] = NonEmptyListExpressionContent(v[1], False)

def p_iterexp_2(v):
    "iterexp : nonemptyiterexp ','"
    v[0] = NonEmptyListExpressionContent(v[1], True)

def p_nonemptyiterexp_1(v):
    "nonemptyiterexp : exp"
    v[0] = NonEmptyListExpressionContent([v[1]], False)

def p_nonemptyiterexp_2(v):
    "nonemptyiterexp : nonemptyiterexp ',' exp"
    v[0] = NonEmptyListExpressionContent(v[1].expressions + [v[3]], False)

def p_dictexp_1(v):
    "dictexp : nonemptydictexp"
    v[0] = NonEmptyDictExpressionContent(v[1], False)

def p_dictexp_2(v):
    "dictexp : nonemptydictexp ','"
    v[0] = NonEmptyDictExpressionContent(v[1], True)

def p_nonemptydictexp_1(v):
    "nonemptydictexp : exp ':' exp"
    v[0] = NonEmptyDictExpressionContent([(v[1], v[3])], True)

def p_nonemptydictexp_2(v):
    "nonemptydictexp : nonemptydictexp ',' exp ':' exp"
    v[0] = NonEmptyDictExpressionContent(v[1].key_value_pairs + [(v[3], v[5])], True)

def p_arguments_1(v):
    "arguments : exp"
    v[0] = "ok"

def p_arguments_2(v):
    "arguments : exp arguments"
    v[0] = "ok"

def p_pattern_1(v):
    "pattern : const"
    v[0] = ConstantPattern(v[1])

def p_pattern_2(v):
    "pattern : '_'"
    v[0] = AnythingPattern()

def p_pattern_3(v):
    "pattern : IDENTIFIER"
    v[0] = IdentifierPatttern(v[1])

def p_pattern_4(v):
    "pattern : '(' pattern ')'"
    v[0] = BracketPattern(v[2])

def p_pattern_5(v):
    "pattern : '(' tuplepattern ')'"
    v[0] = TuplePattern(v[2])

def p_pattern_6(v):
    "pattern : '[' iterpattern ']'"
    v[0] = ListPattern(v[2])

def p_pattern_7(v):
    "pattern : '{' dictpattern '}'"
    v[0] = DictPattern(v[2])

def p_tuplepattern_1(v):
    "tuplepattern : pattern ','"
    v[0] = NonEmptyTuplePatternContent(v[1].patterns, True)

def p_tuplepattern_2(v):
    "tuplepattern : nonsingletuplepattern"
    v[0] = NonEmptyTuplePatternContent(v[1].patterns, False)

def p_tuplepattern_3(v):
    "tuplepattern : nonsingletuplepattern ','"
    v[0] = NonEmptyTuplePatternContent(v[1].patterns, True)

def p_nonsingletuplepattern_1(v):
    "nonsingletuplepattern : pattern ',' pattern"
    v[0] = NonEmptyTuplePatternContent([(v[1], v[3])], False)

def p_nonsingletuplepattern_2(v):
    "nonsingletuplepattern : nonsingletuplepattern ',' pattern"
    v[0] = NonEmptyTuplePatternContent([(v[1], v[3])], False)

def p_iterpattern_1(v):
    "iterpattern : nonemptyiterpattern"
    v[0] = NonEmptyListPatternContent(v[1].patterns, False)

def p_iterpattern_2(v):
    "iterpattern : nonemptyiterpattern ','"
    v[0] = NonEmptyListPatternContent(v[1].patterns, True)

def p_nonemptyiterpattern_1(v):
    "nonemptyiterpattern : pattern"
    v[0] = NonEmptyListPatternContent([v[1]], False)

def p_nonemptyiterpattern_2(v):
    "nonemptyiterpattern : nonemptyiterpattern ',' pattern"
    v[0] = NonEmptyListPatternContent(v[1].patterns + [v[3]], False)

def p_dictpattern_1(v):
    "dictpattern : nonemptydictpattern"
    v[0] = NonEmptyDictPatternContent(v[1], False)

def p_dictpattern_2(v):
    "dictpattern : nonemptydictpattern ','"
    v[0] = NonEmptyDictPatternContent(v[1], True)

def p_nonemptydictpattern_1(v):
    "nonemptydictpattern : pattern ':' pattern"
    v[0] = NonEmptyDictPatternContent([(v[1], v[3])], False)

def p_nonemptydictpattern_2(v):
    "nonemptydictpattern : nonemptydictpattern ',' pattern ':' pattern"
    v[0] = "ok"
