from aeonius_parser import parse
from language.context import Context
from language.grammar import Aeonius
import sys
import inspect
import graphviz

with open("prelude.py", "r") as f:
    prelude = f.read()


def get_importing_module():
    for frame_info in inspect.stack():
        module = inspect.getmodule(frame_info[0])
        if module and module.__name__ != __name__:
            return module

def importCode(code,module):
    exec(code,module.__dict__)


def help():
    print("                aeonius                    ")
    print("     A functional extension for Python     ")
    print("===========================================")
    print()
    print("Valid arguments:")
    print("-h: Get help")
    print("-d: Whether to run on debug mode. In debug")
    print("mode, the compiled python code is printed")
    print("to stdout instead of to a file")
    print("-g: Wheather to generate the language graph.")
    print("This graph will be generated instead of the")
    print("python program")
    print("--input: The input aeonius file")
    print("--output: The python/graph file to write the")
    print("parsed program to")


def parse_args(single_flags, valid_args):

    result = {}

    argv = []

    for s in single_flags:
        result[s[1:]] = False

    # Remove flags that don't take any arguments
    # and process them now
    for str in sys.argv:
        if str in single_flags:
            # Remove initial '-' from string
            result[str[1:]] = True
        else:
            argv = argv + [str]

    # User provided arguments start at index 1 (0 is the process name)
    # In this format arguments are passed as (note we have removed flags that
    # take no arguments)
    # program --flag1 value1 --flag2 value2 ...
    # In this schema, the values are stored in odd positions and flags
    # in even positions.
    # As such, we iterate over the even indices of the argv list
    for i in range(2, len(argv), 2):
        if argv[i - 1] in valid_args:
            # Remove first '--' chars from argv
            result[argv[i - 1][2:]] = argv[i]
        else:
            print(f"Invalid argument {argv[i - 1]}")
            exit(1)

    return result


def transpile(input, debug):
    parsed = parse(prelude + input)

    context = Context()
    context.symbols = Context.stdlib_symbols
    (valid, reasons) = parsed.validate(context)

    if not valid:
        print("Logic error in code")
        for reason in reasons:
            print(reason)
        exit(-1)

    with open("aeonius_stdlib.py", "r") as f:
        stdlib = f.read()

    context = Context()
    context.symbols = Context.stdlib_symbols

    if debug:
        return (parsed.to_python(context),context)
    else:
        return (stdlib + parsed.to_python(context),context)


def main():
    single = [
        "-h",
        "-d",
        "-g"
    ]

    valid_arguments = [
        "--input",
        "--output"
    ]

    args = parse_args(single, valid_arguments)

    if args["h"]:
        help()
        return

    with open(args["input"], "r") as f:
        data = f.read()
    
    if args["g"]:
        parsed = parse(input)
        dot = graphviz.Digraph()
        parsed.append_to_graph(dot)
        dot.render(args["output"], view=False, format='png')
        return

    parsed = transpile(data, args["d"])[0]

    if (args["d"]):
        print(parsed)

    else:
        with open(args["output"], "w") as g:
            g.write(parsed)


def import_main():
    args = parse_args(single, valid_arguments)
    with open(args["input"], "r") as f:
        data = f.read()

    parsed = parse(prelude + data)
    exec(parsed.to_python(Context()))


def include(module):
    with open(module.__file__, "r") as f:
        data = f.read()
        parsed,context = transpile(data, False)
        return importCode(parsed,module.__name__,1)


def includeAE(module):
    with open(module.__file__, "r") as f:
        data = f.read()
        parsed = parse(prelude + data)
        context = Context()
        context.symbols = Context.stdlib_symbols

        (valid, reasons) = parsed.validate(context)

        if not valid:
            print("Logic error in code")
            for reason in reasons:
                print(reason)
            exit(-1)

        context = Context()
        context.symbols = Context.stdlib_symbols

        with open("aeonius_stdlib.py", "r") as f:
            stdlib = f.read()
        parsed.snippets=list(filter(lambda x:isinstance(x, Aeonius),parsed.snippets))
        importCode(stdlib + parsed.to_python(context),module)






if __name__ == "__main__":
    main()
else:
    aeonius_code=includeAE(get_importing_module())
    
    
