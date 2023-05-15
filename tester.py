from test_files import aeonius
from test_files import it50
from test_files import rec50
import main as main
from language.utils import clean_identifier
import re
import time
import json
import sys
sys.setrecursionlimit(10**6)
functionNames={}
for pythonFile in [aeonius,it50,rec50]:
    with open(pythonFile.__file__) as f:
        file=f.read()
        functions=re.findall(r"(#\d+)\n(def (\w+)\(.*\)\:|def (\w+)\:|op \((.*)\)\:|(\w+) =)",file)
        for i in functions:
            if int(i[0][1:]) not in functionNames:
                functionNames[int(i[0][1:])]=[]
            functionNames[int(i[0][1:])].append(pythonFile.__name__[11:]+'.'+i[2]+i[3]+clean_identifier(i[4])+i[5])
functionArguments={
    1:[1,1024],
    2:[1,7,1024],
    3:[list(range(1024)),list(range(1024))],
    4:[list(range(1024)),1023],
    5:[list(range(1024))],
    6:[1000,list(range(1024))],
    7:[1000,list(range(1024))],
    8:[list(range(1024)),list(range(1024))],
    9:[1000,list(range(1024))],
    10:[1000,1],
    11:[2,list(range(1024))],
    12:[[i%100 for i in range(1024)]],
    13:[[list(range(i,i+1024)) for i in range(20)]],
    14:[list(range(1024))],
    15:[list(range(1024))],
    16:[list(range(1024)),list(range(1024))],
    17:[list(range(1024)),list(range(1024))],
    18:[[1021,1022,1023],list(range(1024))],
    19:[4,[i%5 for i in range(1024)]],
    20:[list(range(1024))],
    21:[4,[i%5 for i in range(1024)]],
    22:[[4],[i%5 for i in range(1024)]],
    23:[list(range(1024)),list(range(1024))],
    24:[list(range(1,1024)),list(range(1024))],
    25:[4548,list(range(4852))],
    26:[[["o","l","a"],["v","a","s","q","u","e","s"],["t","u"],["é","s"],["b","a","s","t","a","n","t","e"],["m","a","l","u","c","o"],["c","a","s","o"],["n","a","o"],["s","a","i","b","a","s"]]],
    27:[[["o","l","a"],["v","a","s","q","u","e","s"],["t","u"],["é","s"],["b","a","s","t","a","n","t","e"],["m","a","l","u","c","o"],["c","a","s","o"],["n","a","o"],["s","a","i","b","a","s"]]],
    28:[list(range(1,1024))],
    29:[list(range(1,1024))],
    30:[["v","4","5","q","u","3","5"]],
    31:[list(range(1,1024))],
    32:[list(range(1,1024))],
    33:[list(range(1,1024))],
    34:[list(range(1,1024))[::-1]],
    35:[["o","t","o","r","r","i","n","o","l","a","r","i","g","u","l","o","g","i","s","t","a"],["o","t","o","r","r","i","n","o","l","a","r","i","g","u","l","o","g","i","s","t","a","1"]],
    36:["i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]],
    37:[[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]],
    38:[[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]],
    39:["i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]],
    40:["i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]],
    41:[["a","a","b","b","b","c","c","c","c","d","d","d","d","d","e","e","e","e","e","e","f","f","f","f","f","f"]],
    42:[[{1:1},{2:1},{1:2},{2:2},{1:3},{2:3},{1:4},{1:5},{2:4},{2:5}]],
    43:[[1,2,3,None,1,2,3,None,None,None,2,3]],
    44:[(5,5),[['N', 'o', 'r', 't', 'e'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['O', 'e', 's', 't', 'e'],['E', 's', 't', 'e']]],
    45:[(5,5),(8,10)],
    46:[[['N', 'o', 'r', 't', 'e'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['N', 'o', 'r', 't', 'e'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['N', 'o', 'r', 't', 'e'],['N', 'o', 'r', 't', 'e'],['S', 'u', 'l'],['O', 'e', 's', 't', 'e'],['S', 'u', 'l']]],
    47:[[(1,1),(1,2),(2,1),(3,1),(1,3),(4,4),(4,1),(1,4),(6,6)]],
    48:[(1,3),[(1,1),(1,2),(2,1),(3,1),(1,3),(4,4),(4,1),(1,4),(6,6)]],
    49:[[(1,1),(1,2),(2,1),(3,1),(1,3),(4,4),(4,1),(1,4),(6,6)]],
    50:[[['A', 'm', 'a', 'r', 'e', 'l', 'o'],['V', 'e', 'r', 'd', 'e'],['A', 'm', 'a', 'r', 'e', 'l', 'o'],['V', 'e', 'r', 'd', 'e'],['V', 'e', 'r', 'm', 'e', 'l', 'h', 'o'],['V', 'e', 'r', 'd', 'e'],['A', 'm', 'a', 'r', 'e', 'l', 'o'],['V', 'e', 'r', 'd', 'e'],['V', 'e', 'r', 'm', 'e', 'l', 'h', 'o'],['V', 'e', 'r', 'd', 'e'],['A', 'm', 'a', 'r', 'e', 'l', 'o'],['V', 'e', 'r', 'd', 'e'],['V', 'e', 'r', 'd', 'e'],['A', 'm', 'a', 'r', 'e', 'l', 'o'],['V', 'e', 'r', 'd', 'e']]]
}
results={}

main.aeonius_import(aeonius.__file__)

def argsToFunction(args):
    s=""
    for i in args:
        s= s+"("+str(i)+")"
    return s

for k,v in functionNames.items():
    print(k)
    results[k]={"ae":[],"it":[],"rec":[]}
    input = functionArguments[k]
    for function in v:
        execString=""
        if function.startswith("aeonius"):
            
            execString='main.'+function.split('.')[1]
            execString+=argsToFunction(input)
        else:
            execString+=function
            execString+='('+",".join(map(str,input))+')'
        for iteration in range(10):
            start = time.time()
            exec(execString)
            end = time.time()
            if function.startswith("aeonius"):
                results[k]["ae"].append(end-start)
            elif function.startswith("it50"):
                results[k]["it"].append(end-start)
            else:
                results[k]["rec"].append(end-start)
            
    
with open("test_output.json","w") as f:
    json.dump(results, f)