import os
import filecmp
from aeonius_parser import parse
from language.context import Context
import graphviz


def test():

    with open(f"test_files/aeonius.py") as f:
        input = f.read()
        dot = graphviz.Digraph()
        parsed=parse(input)
        context = Context()
        context.symbols = Context.stdlib_symbols
        parsed.append_to_graph(dot)
        dot.render('graph', view=True, format='png')

if __name__=="__main__":
    test()
