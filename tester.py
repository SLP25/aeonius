from test_files import aeonius
from test_files import it50
from test_files import rec50
from main import aeonius_import
from language.utils import clean_identifier
import re
import pprint
import time
import json
functionNames={}
for pythonFile in [aeonius,it50,rec50]:
    with open(pythonFile.__file__) as f:
        file=f.read()
        functions=re.findall(r"(#\d+)\n(def (\w+)\(.*\)\:|def (\w+)\:|op \((.*)\)\:|(\w+) =)",file)
        for i in functions:
            if int(i[0][1:]) not in functionNames:
                functionNames[int(i[0][1:])]=[]
            functionNames[int(i[0][1:])].append(pythonFile.__name__[11:]+'.'+i[2]+i[3]+clean_identifier(i[4])+i[5])
pprint.pprint(functionNames)
functionArguments={
    1:(1,1024),
    2:(1,7,1024),
    3:(list(range(1024)),list(range(1024))),
    4:(list(range(1024)),1024),
    5:(list(range(1024))),
    6:(1000,list(range(1024))),
    7:(1000,list(range(1024))),
    8:(list(range(1024)),list(range(1024))),
    9:(1000,list(range(1024))),
    10:(1000,'o'),
    11:('o',list(range(1024))),
    12:([i%100 for i in range(1024)]),
    13:([list(range(i,i+1024)) for i in range(20)]),
    14:(list(range(1024))),
    15:(list(range(1024))),
    16:(list(range(1024)),list(range(1024))),
    17:(list(range(1024)),list(range(1024))),
    18:([1021,1022,1023],list(range(1024))),
    19:(4,[i%5 for i in range(1024)]),
    20:(list(range(1024))),
    21:(4,[i%5 for i in range(1024)]),
    22:(4,[i%5 for i in range(1024)]),
    23:(list(range(1024)),list(range(1024))),
    24:(list(range(1,1024)),list(range(1024))),
    25:(4548,list(range(4852))),
    26:(["ola","vasques","tu","és","bastante","maluco","caso","nao","saibas"]),
    27:(["ola","vasques","tu","és","bastante","maluco","caso","nao","saibas"]),
    28:([("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    29:(list(range(1,1024))),
    30:(list(range(1,1024))),
    31:(list(range(1,1024))),
    32:(list(range(1,1024))),
    33:(list(range(1,1024))),
    34:(list(range(1,1024))[::-1]),
    35:("otorrinolarigulogista","otorrinolarigulogista1"),
    36:("i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    37:([("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    38:([("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    39:("i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    40:("i",[("a",2),("b",3),("c",4),("d",5),("e",6),("f",7),("g",8),("h",9),("i",9),("j",2),("k",2),("l",2),("m",2),("n",2)]),
    41:(["a","a","b","b","b","c","c","c","c","d","d","d","d","d","e","e","e","e","e","e","f","f","f","f","f","f"]),
    42:([{"a":1},{"b":1},{"a":2},{"b":2},{"a":3},{"b":3},{"a":4},{"a":5},{"b":4},{"b":5}]),
    43:([1,2,3,None,1,2,3,None,None,None,2,3]),
    44:((5,5),["Norte","Norte","Sul","Oeste","Este"]),
    45:((5,5),(8,10)),
    46:(["Norte","Norte","Sul","Norte","Sul","Norte","Norte","Sul","Norte","Sul","Norte","Norte","Sul","Oeste","Sul"]),
    47:([{"x":1,"y":1},{"x":1,"y":2},{"x":2,"y":1},{"x":3,"y":1},{"x":1,"y":3},{"x":4,"y":4},{"x":4,"y":1},{"x":1,"y":4},{"x":6,"y":6}]),
    48:({"x":1,"y":3},[{"x":1,"y":1},{"x":1,"y":2},{"x":2,"y":1},{"x":3,"y":1},{"x":1,"y":3},{"x":4,"y":4},{"x":4,"y":1},{"x":1,"y":4},{"x":6,"y":6}]),
    49:([{"x":1,"y":1},{"x":1,"y":2},{"x":2,"y":1},{"x":3,"y":1},{"x":1,"y":3},{"x":4,"y":4},{"x":4,"y":1},{"x":1,"y":4},{"x":6,"y":6}]),
    50:(["Amarelo","Verde","Amarelo","Verde","Vermelho","Verde","Amarelo","Verde","Vermelho","Verde","Amarelo","Verde","Verde","Amarelo","Verde"])
}
results={}

aeonius_import(aeonius.__file__)

for k,v in functionNames.items():
    results[k]={"ae":[],"it":[],"rec":[]}
    input = functionArguments[k]
    for function in v:
        execString=""
        if function.startswith("aeonius"):
            ae,fname = function.split('.')
            execString+=fname
            for arg in input:
                execString+='('+f"{arg}"+')'
        else:
            execString+=function
            for arg in input:
                execString+='('+",".join(input)+')'
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