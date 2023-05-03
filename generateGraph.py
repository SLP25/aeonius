import os
import filecmp
from aeonius_parser import parse
import graphviz

def test(file):
    
    with open(f"tests/input/{file}") as f:
        input = f.read()
    dot = graphviz.Digraph() 

    parse(input).append_to_graph(dot)
    dot.render('graph', view=True, format='png')

input_files = set(os.listdir("tests/input/"))
for file in input_files:
    test(file)

