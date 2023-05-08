import os
import filecmp
from aeonius_parser import parse
import graphviz


def test():

    with open(f"test_files/aeonius.ae") as f:
        input = f.read()
    dot = graphviz.Digraph()

    parse(input).append_to_graph(dot)
    dot.render('graph', view=True, format='png')

if __name__=="__main__":
    test()
